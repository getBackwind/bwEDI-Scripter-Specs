# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class ES(Segment):
    """
    ES - Equipment Status
    
    Description:
        To provide detail information regarding the dynamic condition of equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ES/
    """
    _id: Literal["ES"] = id_element(name="ES")

    BadOrderReasonCode: Optional[X12ID] = element(
        name="ES01",
        description="Bad Order Reason Code",
        min_length=1,
        max_length=1,
    )

    HoldReasonCode: Optional[X12ID] = element(
        name="ES02",
        description="Hold Reason Code",
        min_length=2,
        max_length=2,
    )

    AssociationOfAmericanRailroadsCarGradeCode: Optional[X12ID] = element(
        name="ES03",
        description="Association of American Railroads Car Grade Code",
        min_length=1,
        max_length=1,
    )

    TimePeriodQualifier: Optional[X12ID] = element(
        name="ES04",
        description="Time Period Qualifier",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="ES05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    SwitchTypeCode: Optional[X12ID] = element(
        name="ES06",
        description="Switch Type Code",
        min_length=2,
        max_length=2,
    )
