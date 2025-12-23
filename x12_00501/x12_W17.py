# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12TM


class W17(Segment):
    """
    W17 - Warehouse Receipt Identification
    
    Description:
        To provide identifying numbers and date
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W17/
    """
    _id: Literal["W17"] = id_element(name="W17")

    ReportingCode: X12ID = element(
        name="W1701",
        description="Reporting Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="W1702",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    WarehouseReceiptNumber: X12AN = element(
        name="W1703",
        description="Warehouse Receipt Number",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    DepositorOrderNumber: Optional[X12AN] = element(
        name="W1704",
        description="Depositor Order Number",
        min_length=1,
        max_length=22,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="W1705",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    TimeQualifier: Optional[X12ID] = element(
        name="W1706",
        description="Time Qualifier",
        min_length=1,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="W1707",
        description="Time",
        min_length=4,
        max_length=8,
    )

    MasterReferenceLinkNumber: Optional[X12AN] = element(
        name="W1708",
        description="Master Reference (Link) Number",
        min_length=1,
        max_length=22,
    )

    LinkSequenceNumber: Optional[X12Nn] = element(
        name="W1709",
        description="Link Sequence Number",
        min_length=6,
        max_length=6,
    )
