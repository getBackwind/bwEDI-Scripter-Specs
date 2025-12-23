# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CHB(Segment):
    """
    CHB - Chargeback Information
    
    Description:
        To define elements associated with a charge to unemployment insurance tax account
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CHB/
    """
    _id: Literal["CHB"] = id_element(name="CHB")

    LocationQualifier: Optional[X12ID] = element(
        name="CHB01",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="CHB02",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    ReasonStoppedWorkCode: Optional[X12ID] = element(
        name="CHB03",
        description="Reason Stopped Work Code",
        min_length=2,
        max_length=2,
    )

    ClaimTypeCode: Optional[X12ID] = element(
        name="CHB04",
        description="Claim Type Code",
        min_length=1,
        max_length=2,
    )

    ClaimStatusCode: Optional[X12ID] = element(
        name="CHB05",
        description="Claim Status Code",
        min_length=1,
        max_length=2,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="CHB06",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    CreditDebitFlagCode: Optional[X12ID] = element(
        name="CHB07",
        description="Credit/Debit Flag Code",
        min_length=1,
        max_length=1,
    )

    IndustryCode: Optional[X12AN] = element(
        name="CHB08",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    AllowanceOrChargeIndicator: Optional[X12ID] = element(
        name="CHB09",
        description="Allowance or Charge Indicator",
    )
