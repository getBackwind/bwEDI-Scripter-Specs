# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SCA(Segment):
    """
    SCA - Statistical Category Analysis
    
    Description:
        To specify statistical norms and related information associated with testing programs
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SCA/
    """
    _id: Literal["SCA"] = id_element(name="SCA")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="SCA01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="SCA02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    StatisticCode: Optional[X12ID] = element(
        name="SCA03",
        description="Statistic Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="SCA04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="SCA05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    RangeMinimum: Optional[X12R] = element(
        name="SCA06",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="SCA07",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )
