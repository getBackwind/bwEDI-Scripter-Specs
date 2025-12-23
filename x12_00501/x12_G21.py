# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class G21(Segment):
    """
    G21 - Product Information
    
    Description:
        To specify authorize/de-authorize code and product information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G21/
    """
    _id: Literal["G21"] = id_element(name="G21")

    AuthorizeDeAuthorizeCode: X12ID = element(
        name="G2101",
        description="Authorize/ De-Authorize Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="G2102",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    UPCEANConsumerPackageCode: X12AN = element(
        name="G2103",
        description="U.P.C./EAN Consumer Package Code",
        mandatory=True,
        min_length=12,
        max_length=12,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="G2104",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    Pack: Optional[X12Nn] = element(
        name="G2105",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    UnitPrice: Optional[X12R] = element(
        name="G2106",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G2107",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G2108",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    InnerPack: Optional[X12Nn] = element(
        name="G2109",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )

    ItemDistributionCode: Optional[X12ID] = element(
        name="G2110",
        description="Item Distribution Code",
        min_length=2,
        max_length=2,
    )
