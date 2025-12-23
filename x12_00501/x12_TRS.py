# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class TRS(Segment):
    """
    TRS - Tax Rate
    
    Description:
        To provide information for a change in filing requirements for a particular tax type
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TRS/
    """
    _id: Literal["TRS"] = id_element(name="TRS")

    ActionCode: X12ID = element(
        name="TRS01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="TRS02",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="TRS03",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="TRS04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    RateApplicationCode: Optional[X12ID] = element(
        name="TRS05",
        description="Rate Application Code",
        min_length=2,
        max_length=2,
    )
