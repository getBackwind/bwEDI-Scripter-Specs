# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SPA(Segment):
    """
    SPA - Status of Product or Activity
    
    Description:
        To indicate the details and status of a product or product activity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SPA/
    """
    _id: Literal["SPA"] = id_element(name="SPA")

    StatusCode: X12ID = element(
        name="SPA01",
        description="Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="SPA02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="SPA03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="SPA04",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="SPA05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="SPA06",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    StatusReasonCode2: Optional[X12ID] = element(
        name="SPA07",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    StatusReasonCode3: Optional[X12ID] = element(
        name="SPA08",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="SPA09",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    ProductDescriptionCode: Optional[X12AN] = element(
        name="SPA10",
        description="Product Description Code",
        min_length=1,
        max_length=12,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="SPA11",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )
