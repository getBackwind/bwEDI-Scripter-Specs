# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class IT8(Segment):
    """
    IT8 - Conditions of Sale
    
    Description:
        To specify general conditions or requirements and to detail conditions for substitution of alternate products
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IT8/
    """
    _id: Literal["IT8"] = id_element(name="IT8")

    SalesRequirementCode: Optional[X12ID] = element(
        name="IT801",
        description="Sales Requirement Code",
        min_length=1,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="IT802",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="IT803",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    AccountNumber: Optional[X12AN] = element(
        name="IT804",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    Date: Optional[X12DT] = element(
        name="IT805",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="IT806",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    ProductServiceSubstitutionCode: Optional[X12ID] = element(
        name="IT807",
        description="Product/Service Substitution Code",
        min_length=1,
        max_length=2,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="IT808",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="IT809",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="IT810",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="IT811",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="IT812",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="IT813",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier4: Optional[X12ID] = element(
        name="IT814",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="IT815",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier5: Optional[X12ID] = element(
        name="IT816",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID5: Optional[X12AN] = element(
        name="IT817",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier6: Optional[X12ID] = element(
        name="IT818",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID6: Optional[X12AN] = element(
        name="IT819",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier7: Optional[X12ID] = element(
        name="IT820",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID7: Optional[X12AN] = element(
        name="IT821",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier8: Optional[X12ID] = element(
        name="IT822",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID8: Optional[X12AN] = element(
        name="IT823",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier9: Optional[X12ID] = element(
        name="IT824",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID9: Optional[X12AN] = element(
        name="IT825",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier10: Optional[X12ID] = element(
        name="IT826",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID10: Optional[X12AN] = element(
        name="IT827",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
