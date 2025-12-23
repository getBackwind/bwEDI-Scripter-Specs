# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class TIS(Segment):
    """
    TIS - Title Insurance Services
    
    Description:
        To provide the type, extent, and dates for title insurance service
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TIS/
    """
    _id: Literal["TIS"] = id_element(name="TIS")

    TitleInsuranceServicesCode: X12ID = element(
        name="TIS01",
        description="Title Insurance Services Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="TIS02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="TIS03",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="TIS04",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
