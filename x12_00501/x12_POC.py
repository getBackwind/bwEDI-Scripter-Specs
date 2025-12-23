# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class POC(Segment):
    """
    POC - Line Item Change
    
    Description:
        To specify changes to a line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/POC/
    """
    _id: Literal["POC"] = id_element(name="POC")

    AssignedIdentification: Optional[X12AN] = element(
        name="POC01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    ChangeOrResponseTypeCode: X12ID = element(
        name="POC02",
        description="Change or Response Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="POC03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    QuantityLeftToReceive: Optional[X12R] = element(
        name="POC04",
        description="Quantity Left to Receive",
        min_length=1,
        max_length=9,
    )

    UnitPrice: Optional[X12R] = element(
        name="POC06",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    BasisOfUnitPriceCode: Optional[X12ID] = element(
        name="POC07",
        description="Basis of Unit Price Code",
        min_length=2,
        max_length=2,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="POC08",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="POC09",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="POC10",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="POC11",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="POC12",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="POC13",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier4: Optional[X12ID] = element(
        name="POC14",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="POC15",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier5: Optional[X12ID] = element(
        name="POC16",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID5: Optional[X12AN] = element(
        name="POC17",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier6: Optional[X12ID] = element(
        name="POC18",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID6: Optional[X12AN] = element(
        name="POC19",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier7: Optional[X12ID] = element(
        name="POC20",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID7: Optional[X12AN] = element(
        name="POC21",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier8: Optional[X12ID] = element(
        name="POC22",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID8: Optional[X12AN] = element(
        name="POC23",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier9: Optional[X12ID] = element(
        name="POC24",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID9: Optional[X12AN] = element(
        name="POC25",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier10: Optional[X12ID] = element(
        name="POC26",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID10: Optional[X12AN] = element(
        name="POC27",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
