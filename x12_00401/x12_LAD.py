# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class LAD(Segment):
    """
    LAD - Lading Detail
    
    Description:
        To transmit detailed lading data pertinent to a pickup or delivery
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LAD/
    """
    _id: Literal["LAD"] = id_element(name="LAD")

    PackagingFormCode: Optional[X12ID] = element(
        name="LAD01",
        description="Packaging Form Code",
        min_length=3,
        max_length=3,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="LAD02",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="LAD03",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    UnitWeight: Optional[X12R] = element(
        name="LAD04",
        description="Unit Weight",
        min_length=1,
        max_length=8,
    )

    WeightUnitCode2: Optional[X12ID] = element(
        name="LAD05",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="LAD06",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="LAD07",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="LAD08",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="LAD09",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="LAD10",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="LAD11",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="LAD12",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    LadingDescription: Optional[X12AN] = element(
        name="LAD13",
        description="Lading Description",
        min_length=1,
        max_length=50,
    )
