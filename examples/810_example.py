# ##########################################################################
#                               810 Definition
# ##########################################################################

from typing import Optional
from pydantic import Field
from bwEDI import SegmentStruct
from bwEDI.schemes import EdiFlatHeader
from bwEDI.x12_00401 import BIG, IT1, TDS, CTT, REF, ITD, DTM, CTP, SAC, N1, TXI, PID

class Line(SegmentStruct):
    Item: IT1
    Tax: Optional[TXI] = None
    References: Optional[list[REF]] = Field(default_factory=list)


class Summary(SegmentStruct):
    Amount: TDS
    Count: CTT
    Charge: SAC
    Tax: Optional[TXI] = None


class Schema810(SegmentStruct):
    EDI: EdiFlatHeader
    Header: BIG
    Dates: list[DTM] = Field(default_factory=list)
    Lines: list[Line] = Field(min_length=1)
    Summary: Summary




# ##########################################################################
#                               810 Mapper
# ##########################################################################

import bwEDI
from golem_variables import Company
from missions_edi.priority_definitions import Pri810
from .definition import *
from golem.util import now_timezone
from bwEDI.x12_types import as_X12N2, as_X12N0


def handle_810(inv: Pri810, company: Company) -> bytes:

    partner = company.partners[inv.partner_id]

    # ------------------------- HEADER ---------------------------------------

    edi_header = EdiFlatHeader(
        SenderIdQualifier=partner.edi_vendor_code_qualifier,
        SenderID=partner.edi_vendor_code,
        ReceiverIdQualifier=partner.edi_partner_code_qualifier,
        ReceiverID=inv.end_customer_id,
        DocumentType="810",
        FunctionalIdCode="IN",
        GroupID='001',
        TransactionSetID="0001"
    )

    big = BIG(
        InvoiceDate=inv.invoice_date.replace("-", ""),
        InvoiceID=inv.invoice_num,
        PurchaseOrderDate=inv.po_date.replace("-", ""),
        PurchaseOrderID=inv.po_num,
        TransactionType="CN" if inv.total_amount < 0 else "DI",
    )

    # ------------------------- Detail ---------------------------------------

    lines = []

    for i, item in enumerate(inv.item_level):
        line_item = IT1(LineID=i + 1,
                        Quantity=f"{item.quantity:.2f}",
                        UOM=item.uom,
                        UnitPrice=f"{item.price:.2f}",
                        # BasisOfUnitPrice="LE",
                        ItemIdQualifier="VN",
                        ItemID=item.vendor_part_num)

        lines.append(Line(
            Item=line_item,
            # Tax=tax,
        ))

    # ------------------------- SUMMARY ---------------------------------------

    tds = TDS(TotalAmount=as_X12N2(inv.total_amount))

    count = CTT(LineCount=as_X12N0(len(lines)))

    sac = SAC(
        ChargeIndicator="C",
        SpecialServiceCode="D200",
        ReferenceID=inv.trk_number,
        Description=inv.carrier,
    )

    summary = Summary(Amount=tds,
                    Count=count,
                    Charge=sac)

    dates=[DTM(
        DateTimeQualifier="011",
        Date=inv.ship_date.replace("-", "")
        )]

    schema810 = Schema810(
        EDI=edi_header,
        Header=big,
        Dates=dates,
        Lines=lines,
        Summary=summary)

    convertor = bwEDI.EDI()
    convertor.flat(flat_header=edi_header, body=schema810)
    edi_str = convertor.as_edi(pretty=False)
    return edi_str.encode()
