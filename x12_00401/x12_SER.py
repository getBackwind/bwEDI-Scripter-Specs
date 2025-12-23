# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SER(Segment):
    """
    SER - Service Charges
    
    Description:
        To specify the details of the service charges levied
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SER/
    """
    _id: Literal["SER"] = id_element(name="SER")

    ProductServiceIDQualifier: X12ID = element(
        name="SER01",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="SER02",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="SER03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="SER04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    UnitPrice: Optional[X12R] = element(
        name="SER05",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    Quantity: Optional[X12R] = element(
        name="SER06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="SER07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    PriceIdentifierCode: Optional[X12ID] = element(
        name="SER08",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="SER09",
        description="Payment Method Code",
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="SER10",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="SER11",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
