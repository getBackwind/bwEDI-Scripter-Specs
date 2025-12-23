# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SV6(Segment):
    """
    SV6 - Anesthesia Service
    
    Description:
        To specify the claim service detail for anesthesia
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SV6/
    """
    _id: Literal["SV6"] = id_element(name="SV6")

    FacilityCodeQualifier: Optional[X12ID] = element(
        name="SV602",
        description="Facility Code Qualifier",
        min_length=1,
        max_length=1,
    )

    FacilityCodeValue: Optional[X12AN] = element(
        name="SV603",
        description="Facility Code Value",
        min_length=1,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="SV604",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="SV606",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SV607",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
