# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class APR(Segment):
    """
    APR - Association of American Railroads Pool Code Restrictions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/APR/
    """
    _id: Literal["APR"] = id_element(name="APR")

    YesNoConditionOrResponseCode: X12ID = element(
        name="APR01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AssociationOfAmericanRailroadsAARPoolCode: X12ID = element(
        name="APR02",
        description="Association of American Railroads (AAR) Pool Code",
        mandatory=True,
        min_length=7,
        max_length=7,
    )

    AssociationOfAmericanRailroadsAARPoolCode2: Optional[X12ID] = element(
        name="APR03",
        description="Association of American Railroads (AAR) Pool Code",
        min_length=7,
        max_length=7,
    )
