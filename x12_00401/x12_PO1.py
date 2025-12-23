# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PO1(Segment):
    """
    PO1 - Baseline Item Data
    
    Description:
        To specify basic and most frequently used line item data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PO1/
    """
    _id: Literal["PO1"] = id_element(name="PO1")

    LineID: Optional[X12AN] = element(
        name="PO101",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Quantity: Optional[X12R] = element(
        name="PO102",
        description="Quantity Ordered",
        min_length=1,
        max_length=15,
    )

    UOM: Optional[X12ID] = element(
        name="PO103",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UnitPrice: Optional[X12R] = element(
        name="PO104",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    UnitPriceCode: Optional[X12ID] = element(
        name="PO105",
        description="Basis of Unit Price Code",
        min_length=2,
        max_length=2,
    )

    ItemIdQualifier: Optional[X12ID] = element(
        name="PO106",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID: Optional[X12AN] = element(
        name="PO107",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier2: Optional[X12ID] = element(
        name="PO108",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID2: Optional[X12AN] = element(
        name="PO109",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier3: Optional[X12ID] = element(
        name="PO110",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID3: Optional[X12AN] = element(
        name="PO111",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier4: Optional[X12ID] = element(
        name="PO112",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID4: Optional[X12AN] = element(
        name="PO113",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier5: Optional[X12ID] = element(
        name="PO114",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID5: Optional[X12AN] = element(
        name="PO115",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="PO116",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="PO117",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="PO118",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="PO119",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="PO120",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="PO121",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier4: Optional[X12ID] = element(
        name="PO122",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="PO123",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier5: Optional[X12ID] = element(
        name="PO124",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID5: Optional[X12AN] = element(
        name="PO125",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
