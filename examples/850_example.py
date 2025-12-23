# ##########################################################################
#                               850 Definition
# ##########################################################################

from datetime import datetime
from typing import Optional
from bwEDI import SegmentStruct, EDI, EdiFlatHeader
from bwEDI.x12_00401 import AMT, BEG, CTT, REF, MSG, N1, N2, N3, N4, PER, PO1, PID, GS, ST, ITD, CTB, SAC, CN1, N9, NTE


class Address(SegmentStruct):
    Header: N1
    ExtraNames: Optional[N2] = None
    AddressLines: Optional[N3] = None
    Location: Optional[N4] = None


class Instruction(SegmentStruct):
    Instruction: N9
    Messages: list[MSG] = None


class Summary(SegmentStruct):
    Count: CTT
    Amount: AMT
    Charge: Optional[SAC] = None  # ???: optional?


class PurchaseOrderLine(SegmentStruct):
    Item: PO1
    Descriptions: list[PID]
    CostConcession: Optional[CN1] = None


class Schema850(SegmentStruct):
    EDI: EdiFlatHeader
    Header: BEG
    Notes: list[NTE]
    PaymentTerms: ITD
    ShipmentRestrictions: list[CTB]
    References: list[REF]
    Addresses: list[Address]
    Instructions: list[Instruction]
    Contacts: list[PER]
    PurchaseOrderLines: list[PurchaseOrderLine]
    Summary: Summary


def edi_to_json_850(edi_str: str) -> Schema850:
    edi = EDI()
    edi.from_edi(edi_str)

    gs: GS = edi.lookup(GS)[0]
    st: ST = edi.lookup(ST)[0]

    edi_header = EdiFlatHeader(
            SenderIdQualifier=edi.interchange.header.SenderIdQualifier,
            SenderID=edi.interchange.header.SenderID,
            ReceiverIdQualifier=edi.interchange.header.ReceiverIdQualifier,
            ReceiverID=edi.interchange.header.ReceiverID,
            Time=edi.interchange.header.Time,
            Date=datetime.strptime(edi.interchange.header.Date, "%y%m%d").strftime(
                "%Y%m%d"
            ),
            DocumentType="850",
            FunctionalIdCode="IN",
            GroupID=gs.GroupID,
            TransactionSetID=st.TransactionSetID,
        )

    segments = edi.segments()

    # -------------------------------------------- Header ------------------------------------------

    header = edi.lookup(BEG)[0]

    instructions = []
    for i, n9 in edi.enumerate(N9):
        if n9 is None:
            break
        counter = i + 1
        msgs = []
        while isinstance(segments[counter], MSG):
            msg = segments[counter]
            msgs.append(msg)
            counter += 1

        instructions.append(Instruction(Instruction=n9, Messages=msgs))

    addresses = []
    for i, n1 in edi.enumerate(N1):
        if n1 is None:
            break

        n3, n4 = None, None
        counter = i + 1

        while isinstance(segments[counter], (N2, N3, N4)):
            if isinstance(segments[counter], N2):
                n2 = segments[counter]
            elif isinstance(segments[counter], N3):
                n3 = segments[counter]
            elif isinstance(segments[counter], N4):
                n4 = segments[counter]
            counter += 1

        addresses.append(
            Address(Header=n1, ExtraNames=n2, AddressLines=n3, Location=n4)
        )

    # -------------------------------------------- Detail ------------------------------------------
    # Item loop: PO1, PID
    po_lines = []

    for i, po1 in edi.enumerate(PO1):
        if po1 is None:
            break

        descriptions = []
        counter = i + 1
        while isinstance(segments[counter], PID):
            pid = segments[counter]
            descriptions.append(pid)
            counter += 1

        po_lines.append(PurchaseOrderLine(Item=po1, Descriptions=descriptions))

    # -------------------------------------------- Summary ---------------------------------------
    ctt = edi.lookup(CTT)
    amt = edi.lookup(AMT)
    sac = edi.lookup(SAC)

    summary = Summary(
        Count=ctt[0] if sac else None,
        Amount=amt[0] if sac else None,
        Charge=sac[0] if sac else None,
        )

    itd = edi.lookup(ITD)
    ctb = edi.lookup(CTB)

    res = Schema850(
        EDI=edi_header,
        Header=header,
        Notes=edi.lookup(NTE),
        PaymentTerms=itd[0] if itd else None,
        ShipmentRestrictions=ctb[0] if ctb else None,
        References=edi.lookup(REF),
        Addresses=addresses,
        Instructions=instructions,
        Contacts=edi.lookup(PER),
        PurchaseOrderLines=po_lines,
        Summary=summary,
    )

    return res




# ##########################################################################
#                               850 Mapper
# ##########################################################################


from typing import List
from golem.util import now_timezone
from missions.priority_definitions import Pri850, Pri850Item
from .definition import *

def mapper_850(edi_text: str, file_name: str) -> Pri850:
    """
    Converts a single Schema850 object into a Pri850 object,
    reflecting the same logic found in the Golang 850.go code.
    """

    # 1) Convert raw EDI → MultiSchema850
    schema = edi_to_json_850(edi_text)

    edi_header = schema.EDI  # EdiFlatHeader
    beg = schema.Header

    if schema.Addresses:
        addr_seg: Address = schema.Addresses[0]  # Assuming only one address for now
        # if addr_seg.Header:
        #     addr_name = addr_seg.Header.Name or ""
        #     addr_type = addr_seg.Header.TypeCode if addr_seg.Header else ""

        # addr1 = addr_seg.AddressLines.AddressLine1 if addr_seg.AddressLines else ""
        # addr2 = addr_seg.AddressLines.AddressLine2 if addr_seg.AddressLines else ""
        # city = addr_seg.Location.City if addr_seg.Location else ""
        # state = addr_seg.Location.State if addr_seg.Location else ""
        # country = addr_seg.Location.Country if addr_seg.Location else ""
        # zip = addr_seg.Location.PostalCode if addr_seg.Location else ""
    else:
        addr_seg = None

    contact: PER = schema.Contacts[0] if schema.Contacts else None

    #======================== PurchaseOrderLines =======================
    item_list: List[Pri850Item] = []

    for i, pol in enumerate(schema.PurchaseOrderLines or []):
        if not isinstance(pol, PurchaseOrderLine):
            continue

        # Build the final item
        pri_item = Pri850Item(
            line = i+1,  # Line Number
            po_line = pol.Item.LineID or "",  # PO101
            item_id = pol.Item.ItemID,
            quantity = float(pol.Item.Quantity),         # PO102
            uom = pol.Item.UOM or "",                          # PO103
            price = float(pol.Item.UnitPrice),           # PO104
            id_qualif = pol.Item.ItemIdQualifier,
            description = pol.Descriptions[0] if pol.Descriptions else "N/A"  # Part description,
        )

        item_list.append(pri_item)

    #========================== Assemble Pri850 ==============================
    pri850 = Pri850(
        sender_id = "DSSI", #  edi_header.SenderID,
        end_customer_id = edi_header.SenderID or "",  # edi_header.EndCustomerID,
        po_num = beg.PurchaseOrderNumber or "",
        purpose_code = beg.PurposeCode or "",
        purpose_type=beg.TypeCode or "",
        po_date=beg.Date or "",  # "YYYYMMDD"
        cust_po="",
        terms_type = "",
        terms_base_date_code = "",
        contact_type = contact.ContactTypeCode if contact else "",
        contact_name = contact.Name if contact else "",
        id_code_qual = addr_seg.Header.IdCodeQualifier,
        id_code = addr_seg.Header.IdCode,
        addr_name = addr_seg.Header.Name if addr_seg.Header else "",
        addr_type = addr_seg.Header.TypeCode if addr_seg.Header else "",
        addr1 = addr_seg.AddressLines.AddressLine1 if addr_seg.AddressLines else "",
        addr2 = addr_seg.AddressLines.AddressLine2 if addr_seg.AddressLines else "",
        city = addr_seg.Location.City if addr_seg.Location else "",
        state = addr_seg.Location.State if addr_seg.Location else "",
        country = addr_seg.Location.Country if addr_seg.Location else "",
        zip = addr_seg.Location.PostalCode if addr_seg.Location else "",
        fob_pay_code = "",
        restrict = "",
        total_amount = schema.Summary.Amount.TotalAmount,
        total_lines = len(item_list),
        source_file = file_name,
        write_status = "New",
        write_msg = "",  # Add appropriate mapping if available
        write_time = now_timezone().isoformat(),
        lines = item_list,
    )

    return [(pri850, schema)]
