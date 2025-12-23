# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G43(Segment):
    """
    G43 - Promotion/Price List Area
    
    Description:
        To specify the geographic area in which a promotion or price is in effect
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G43/
    """
    _id: Literal["G43"] = id_element(name="G43")

    MarketAreaCodeQualifier: X12ID = element(
        name="G4301",
        description="Market Area Code Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    MarketAreaCodeIdentifier: Optional[X12AN] = element(
        name="G4302",
        description="Market Area Code Identifier",
        min_length=1,
        max_length=13,
    )

    Description: Optional[X12AN] = element(
        name="G4303",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ClassOfTradeCode: Optional[X12ID] = element(
        name="G4304",
        description="Class of Trade Code",
        min_length=2,
        max_length=2,
    )
