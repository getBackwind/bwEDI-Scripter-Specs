# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PCS(Segment):
    """
    PCS - Product Claim Status
    
    Description:
        To convey the status of a product service claim or claims or to supply adjustment reason codes and amounts as needed for an entire claim or for a particular item within the claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PCS/
    """
    _id: Literal["PCS"] = id_element(name="PCS")

    ClaimStatusCode: Optional[X12ID] = element(
        name="PCS01",
        description="Claim Status Code",
        min_length=1,
        max_length=2,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="PCS02",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="PCS03",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    ClaimResponseReasonCode: Optional[X12ID] = element(
        name="PCS04",
        description="Claim Response Reason Code",
        min_length=2,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PCS05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    FollowUpActionCode: Optional[X12ID] = element(
        name="PCS06",
        description="Follow-up Action Code",
        min_length=1,
        max_length=1,
    )

    AgencyQualifierCode2: Optional[X12ID] = element(
        name="PCS07",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier2: Optional[X12AN] = element(
        name="PCS08",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    DispositionCode: Optional[X12AN] = element(
        name="PCS09",
        description="Disposition Code",
        min_length=3,
        max_length=3,
    )

    Description: Optional[X12AN] = element(
        name="PCS10",
        description="Description",
        min_length=1,
        max_length=80,
    )

    AuthorizationIdentification: Optional[X12AN] = element(
        name="PCS11",
        description="Authorization Identification",
        min_length=1,
        max_length=4,
    )
