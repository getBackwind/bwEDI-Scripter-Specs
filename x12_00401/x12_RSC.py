# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RSC(Segment):
    """
    RSC - Resource
    
    Description:
        To identify resource details for tasks or activities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RSC/
    """
    _id: Literal["RSC"] = id_element(name="RSC")

    ResourceCodeOrIdentifier: X12AN = element(
        name="RSC01",
        description="Resource Code (or Identifier)",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    Description: Optional[X12AN] = element(
        name="RSC02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ResourceType: Optional[X12ID] = element(
        name="RSC03",
        description="Resource Type",
    )

    ActionCode: Optional[X12ID] = element(
        name="RSC04",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
