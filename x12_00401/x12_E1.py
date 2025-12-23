# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class E1(Segment):
    """
    E1 - Empty Car Disposition - Pended Destination Consignee
    
    Description:
        To identify the party receiving the empty car
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/E1/
    """
    _id: Literal["E1"] = id_element(name="E1")

    Name30CharacterFormat: X12AN = element(
        name="E101",
        description="Name (30 Character Format)",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="E102",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="E103",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
