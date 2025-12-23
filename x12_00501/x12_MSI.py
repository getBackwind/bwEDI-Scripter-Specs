# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class MSI(Segment):
    """
    MSI - Multi-stop Shipment Information
    
    Description:
        To specify multi-stop shipment information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MSI/
    """
    _id: Literal["MSI"] = id_element(name="MSI")

    YesNoConditionOrResponseCode: X12ID = element(
        name="MSI01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    StopSequenceNumber: Optional[X12Nn] = element(
        name="MSI02",
        description="Stop Sequence Number",
        min_length=1,
        max_length=3,
    )
