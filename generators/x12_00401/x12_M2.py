# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class M2(Segment):
    """
    M2 - Sales/Delivery Terms
    
    Description:
        To state terms and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/M2/
    """
    _id: Literal["M2"] = id_element(name="M2")

    SalesTermsCode: X12ID = element(
        name="M201",
        description="Sales Terms Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    SalesReferenceNumber: Optional[X12AN] = element(
        name="M202",
        description="Sales Reference Number",
        min_length=4,
        max_length=6,
    )

    SalesReferenceDate: Optional[X12DT] = element(
        name="M203",
        description="Sales Reference Date",
        min_length=8,
        max_length=8,
    )

    TransportationTermsCode: Optional[X12ID] = element(
        name="M204",
        description="Transportation Terms Code",
        min_length=3,
        max_length=3,
    )

    SalesComment: Optional[X12AN] = element(
        name="M205",
        description="Sales Comment",
        min_length=2,
        max_length=30,
    )

    DeliveryDate: Optional[X12DT] = element(
        name="M206",
        description="Delivery Date",
        min_length=8,
        max_length=8,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="M207",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="M208",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )
