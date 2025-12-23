# ##########################################################################
#                               855 Definition
# ##########################################################################


from typing import Optional
from bwEDI import SegmentStruct
from bwEDI.schemes import EdiFlatHeader
from bwEDI.x12_00401 import BAK, PO1, ACK, CTT, AMT


class Product(SegmentStruct):
    Header: PO1
    Acknowledgement: ACK


class Summary(SegmentStruct):
    Count: CTT
    Amount: Optional[AMT] = None


class Schema855(SegmentStruct):
    EDI: EdiFlatHeader
    Header: BAK
    Products: list[Product]
    Summary: Summary


# ##########################################################################
#                               855 Mapper
# ##########################################################################

from datetime import datetime
import bwEDI
from golem.util import stringify_number
from golem_variables import Company
from missions.priority_definitions import Pri855
from .definition import *


def handle_855(confirms: Pri855, company: Company) -> bytes:

    partner = company.partners[confirms.partner_id]

    products = []
    lines = 0

    #************* Products *************

    # loop over Priority items, generate item and add to items list
    for pri_item in confirms.items:

        # skip items with quantity 0 or part number empty
        if pri_item.quantity == 0 or pri_item.vendor_part_num == "":
            continue

        lines += 1  # number of line items

        po1 = PO1(
            LineID=str(lines),
            Quantity=stringify_number(pri_item.quantity),
            UOM="EA",
            UnitPrice=f"{pri_item.price:.2f}",
            ItemIdQualifier="VN",
            ItemID=pri_item.vendor_part_num,
        )

        ack = ACK(
            ItemStatus="IA", # maybe use pri_item.item_status
            DateTimeQualifier='068',
            Date=pri_item.due_date.replace("-", ""),  # pri_item.due_date,
        )

        # combine item elements into item struct
        product = Product(
            Header=po1,
            Acknowledgement=ack,
        )

        products.append(product)  # add item to items list

    if not products:
        raise ValueError(f"No items to confirm for PO {confirms.po_num}")

    # ************ Header ************

    bak=BAK(
        TransactionSetPurpose="04", # "00" = Original Purchase Order; "04" = Revised Purchase Order
        TransactionSetControlNumber="1",
        Acknowledgment="AC", # "AC" = Acknowledgment; "RE" = Rejected
        PurchaseOrderID=confirms.po_num,
        PurchaseOrderDate=confirms.po_date,
        ReferenceID=confirms.iv,
        AcknowledgmentDate=datetime.strptime(confirms.ack_date, "%Y-%m-%d").strftime("%Y%m%d"),
    )

    # ************ Summary ************

    amt=AMT(
        AmountQualifier="TT",
        TotalAmount=f"{confirms.amount:.2f}"
    )

    ctt=CTT(
        LineCount=lines
    )

    summary=Summary(
        Count=ctt,
        Amount=amt,
    )

    # ===================== EDI PART =====================

    edi = EdiFlatHeader(
        SenderIdQualifier=partner.edi_vendor_code_qualifier,
        SenderID=partner.edi_vendor_code,
        ReceiverIdQualifier=partner.edi_partner_code_qualifier,
        ReceiverID=confirms.end_customer_id,
        DocumentType="855",
        FunctionalIdCode="PR",
        GroupID='001',
        TransactionSetID="0001"
    )

    # ===================== SCHEMA PART ==================
    schema855 = Schema855(
        EDI = edi,
		Header = bak,
		Products = products,
        Summary=summary,
    )

    convertor = bwEDI.EDI()
    convertor.flat(flat_header=edi, body=schema855)
    edi_str = convertor.as_edi(pretty=False)
    return edi_str.encode()

