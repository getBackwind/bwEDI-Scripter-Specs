# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class IT1(Segment):
    """
    IT1 - Baseline Item Data (Invoice)
    
    Description:
        To specify the basic and most frequently used line item data for the invoice and related transactions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IT1/
    """
    _id: Literal["IT1"] = id_element(name="IT1")

    LineID: Optional[X12AN] = element(
        name="IT101",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Quantity: Optional[X12R] = element(
        name="IT102",
        description="Quantity Invoiced",
        min_length=1,
        max_length=15,
    )

    UOM: Optional[X12ID] = element(
        name="IT103",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UnitPrice: Optional[X12R] = element(
        name="IT104",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    BasisOfUnitPrice: Optional[X12ID] = element(
        name="IT105",
        description="Basis of Unit Price Code",
        min_length=2,
        max_length=2,
    )

    ItemIdQualifier: Optional[X12ID] = element(
        name="IT106",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID: Optional[X12AN] = element(
        name="IT107",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="IT108",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="IT109",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="IT110",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="IT111",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="IT112",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="IT113",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier4: Optional[X12ID] = element(
        name="IT114",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="IT115",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier5: Optional[X12ID] = element(
        name="IT116",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID5: Optional[X12AN] = element(
        name="IT117",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier6: Optional[X12ID] = element(
        name="IT118",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID6: Optional[X12AN] = element(
        name="IT119",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier7: Optional[X12ID] = element(
        name="IT120",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID7: Optional[X12AN] = element(
        name="IT121",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier8: Optional[X12ID] = element(
        name="IT122",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID8: Optional[X12AN] = element(
        name="IT123",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier9: Optional[X12ID] = element(
        name="IT124",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID9: Optional[X12AN] = element(
        name="IT125",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
