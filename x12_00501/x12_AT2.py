# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class AT2(Segment):
    """
    AT2 - Bill of Lading Line Item Detail
    
    Description:
        To specify Bill of Lading quantity, weight, commodity classification and other details.
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AT2/
    """
    _id: Literal["AT2"] = id_element(name="AT2")

    LadingQuantity: Optional[X12Nn] = element(
        name="AT201",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    PackagingFormCode: Optional[X12ID] = element(
        name="AT202",
        description="Packaging Form Code",
        min_length=3,
        max_length=3,
    )

    WeightQualifier: X12ID = element(
        name="AT203",
        description="Weight Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: X12ID = element(
        name="AT204",
        description="Weight Unit Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Weight: X12R = element(
        name="AT205",
        description="Weight",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    LadingQuantity2: Optional[X12Nn] = element(
        name="AT206",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    PackagingFormCode2: Optional[X12ID] = element(
        name="AT207",
        description="Packaging Form Code",
        min_length=3,
        max_length=3,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="AT208",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="AT209",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    FreightClassCode: Optional[X12AN] = element(
        name="AT210",
        description="Freight Class Code",
        min_length=2,
        max_length=5,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="AT211",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    LadingValue: Optional[X12R] = element(
        name="AT212",
        description="Lading Value",
        min_length=2,
        max_length=9,
    )
