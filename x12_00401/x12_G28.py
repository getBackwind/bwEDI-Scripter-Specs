# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G28(Segment):
    """
    G28 - Line Item Numbers
    
    Description:
        To provide basic product identification information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G28/
    """
    _id: Literal["G28"] = id_element(name="G28")

    UPCCaseCode: Optional[X12AN] = element(
        name="G2801",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    UPCEANConsumerPackageCode: Optional[X12AN] = element(
        name="G2802",
        description="U.P.C./EAN Consumer Package Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G2803",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G2804",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="G2805",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="G2806",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
