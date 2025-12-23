# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LH3(Segment):
    """
    LH3 - Hazardous Material Shipping Name Information
    
    Description:
        To specify the hazardous material shipping name and additional descriptive requirements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LH3/
    """
    _id: Literal["LH3"] = id_element(name="LH3")

    HazardousMaterialShippingName: Optional[X12AN] = element(
        name="LH301",
        description="Hazardous Material Shipping Name",
        min_length=1,
        max_length=25,
    )

    HazardousMaterialShippingNameQualifier: Optional[X12ID] = element(
        name="LH302",
        description="Hazardous Material Shipping Name Qualifier",
        min_length=1,
        max_length=1,
    )

    NOSIndicatorCode: Optional[X12ID] = element(
        name="LH303",
        description="N.O.S. Indicator Code",
        min_length=3,
        max_length=3,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="LH304",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
