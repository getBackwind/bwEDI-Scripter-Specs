# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class DIS(Segment):
    """
    DIS - Discount Detail
    
    Description:
        To specify the exact type and terms of various discount information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DIS/
    """
    _id: Literal["DIS"] = id_element(name="DIS")

    DiscountTermsTypeCode: X12ID = element(
        name="DIS01",
        description="Discount Terms Type Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DiscountBaseQualifier: X12ID = element(
        name="DIS02",
        description="Discount Base Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DiscountBaseValue: X12R = element(
        name="DIS03",
        description="Discount Base Value",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    DiscountControlLimitQualifier: X12ID = element(
        name="DIS04",
        description="Discount Control Limit Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DiscountControlLimit: X12Nn = element(
        name="DIS05",
        description="Discount Control Limit",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    DiscountControlLimit2: Optional[X12Nn] = element(
        name="DIS06",
        description="Discount Control Limit",
        min_length=1,
        max_length=10,
    )
