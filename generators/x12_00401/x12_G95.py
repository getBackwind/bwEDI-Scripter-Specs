# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G95(Segment):
    """
    G95 - Performance Requirements
    
    Description:
        To specify the "AND"or "OR"condition for the option, or provide information related to the promotion performance conditions and allocations required, or both
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G95/
    """
    _id: Literal["G95"] = id_element(name="G95")

    PromotionConditionQualifier: Optional[X12ID] = element(
        name="G9501",
        description="Promotion Condition Qualifier",
        min_length=2,
        max_length=2,
    )

    PromotionConditionCode: X12ID = element(
        name="G9502",
        description="Promotion Condition Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="G9503",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )

    Quantity: Optional[X12R] = element(
        name="G9504",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G9505",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="G9506",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Number: Optional[X12Nn] = element(
        name="G9507",
        description="Number",
        min_length=1,
        max_length=9,
    )
