# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class TD1(Segment):
    """
    TD1 - Carrier Details (Quantity and Weight)
    
    Description:
        To specify the transportation details relative to commodity, weight, and quantity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TD1/
    """
    _id: Literal["TD1"] = id_element(name="TD1")

    PackagingCode: Optional[X12AN] = element(
        name="TD101",
        description="Packaging Code",
        min_length=3,
        max_length=5,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="TD102",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    CommodityCodeQualifier: Optional[X12ID] = element(
        name="TD103",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="TD104",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    LadingDescription: Optional[X12AN] = element(
        name="TD105",
        description="Lading Description",
        min_length=1,
        max_length=50,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="TD106",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="TD107",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UomCode: Optional[X12ID] = element(
        name="TD108",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="TD109",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="TD110",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
