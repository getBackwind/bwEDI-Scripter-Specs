# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BSN(Segment):
    """
    BSN - Beginning Segment for Ship Notice
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BSN/
    """
    _id: Literal["BSN"] = id_element(name="BSN")

    PurposeCode: X12ID = element(
        name="BSN01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ShipmentID: X12AN = element(
        name="BSN02",
        description="Shipment Identification",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    ShipDate: X12DT = element(
        name="BSN03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ShipTime: X12TM = element(
        name="BSN04",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    HierarchicalStructureCode: Optional[X12ID] = element(
        name="BSN05",
        description="Hierarchical Structure Code",
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BSN06",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="BSN07",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )
