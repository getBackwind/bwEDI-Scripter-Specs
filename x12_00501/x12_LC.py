# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LC(Segment):
    """
    LC - Life Coverage
    
    Description:
        To provide information on life coverage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LC/
    """
    _id: Literal["LC"] = id_element(name="LC")

    MaintenanceTypeCode: X12ID = element(
        name="LC01",
        description="Maintenance Type Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    MaintenanceReasonCode: Optional[X12ID] = element(
        name="LC02",
        description="Maintenance Reason Code",
        min_length=2,
        max_length=2,
    )

    InsuranceLineCode: Optional[X12ID] = element(
        name="LC03",
        description="Insurance Line Code",
        min_length=2,
        max_length=3,
    )

    PlanCoverageDescription: Optional[X12AN] = element(
        name="LC04",
        description="Plan Coverage Description",
        min_length=1,
        max_length=50,
    )

    Quantity: Optional[X12R] = element(
        name="LC05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ProductOptionCode: Optional[X12ID] = element(
        name="LC06",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="LC07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
