# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R


class PAS(Segment):
    """
    PAS - Property Appraisal Summary
    
    Description:
        To provide high-level information about the property valuation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PAS/
    """
    _id: Literal["PAS"] = id_element(name="PAS")

    PropertyValueEstimateTypeCode: X12ID = element(
        name="PAS01",
        description="Property Value Estimate Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AmountQualifierCode: X12ID = element(
        name="PAS02",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="PAS03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="PAS04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="PAS05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ImprovementStatusCode: Optional[X12ID] = element(
        name="PAS06",
        description="Improvement Status Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PAS07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ConditionIndicator: Optional[X12ID] = element(
        name="PAS08",
        description="Condition Indicator",
    )

    Date: Optional[X12DT] = element(
        name="PAS09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="PAS10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
