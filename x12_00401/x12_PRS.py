# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PRS(Segment):
    """
    PRS - Part Release Status
    
    Description:
        To indicate the status of the part being ordered or forecast with respect to this material release or planning document
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PRS/
    """
    _id: Literal["PRS"] = id_element(name="PRS")

    PartReleaseStatusCode: X12ID = element(
        name="PRS01",
        description="Part Release Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="PRS02",
        description="Description",
        min_length=1,
        max_length=80,
    )
