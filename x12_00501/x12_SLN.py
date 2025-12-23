# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SLN(Segment):
    """
    SLN - Subline Item Detail
    
    Description:
        To specify product subline detail item data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SLN/
    """
    _id: Literal["SLN"] = id_element(name="SLN")

    AssignedIdentification: X12AN = element(
        name="SLN01",
        description="Assigned Identification",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    AssignedIdentification2: Optional[X12AN] = element(
        name="SLN02",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    RelationshipCode: X12ID = element(
        name="SLN03",
        description="Relationship Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="SLN04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitPrice: Optional[X12R] = element(
        name="SLN06",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    BasisOfUnitPriceCode: Optional[X12ID] = element(
        name="SLN07",
        description="Basis of Unit Price Code",
        min_length=2,
        max_length=2,
    )

    RelationshipCode2: Optional[X12ID] = element(
        name="SLN08",
        description="Relationship Code",
        min_length=1,
        max_length=1,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="SLN09",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="SLN10",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="SLN11",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="SLN12",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="SLN13",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="SLN14",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier4: Optional[X12ID] = element(
        name="SLN15",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="SLN16",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier5: Optional[X12ID] = element(
        name="SLN17",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID5: Optional[X12AN] = element(
        name="SLN18",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier6: Optional[X12ID] = element(
        name="SLN19",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID6: Optional[X12AN] = element(
        name="SLN20",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier7: Optional[X12ID] = element(
        name="SLN21",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID7: Optional[X12AN] = element(
        name="SLN22",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier8: Optional[X12ID] = element(
        name="SLN23",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID8: Optional[X12AN] = element(
        name="SLN24",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier9: Optional[X12ID] = element(
        name="SLN25",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID9: Optional[X12AN] = element(
        name="SLN26",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier10: Optional[X12ID] = element(
        name="SLN27",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID10: Optional[X12AN] = element(
        name="SLN28",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
