# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SV3(Segment):
    """
    SV3 - Dental Service
    
    Description:
        To specify the service line item detail for dental work
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SV3/
    """
    _id: Literal["SV3"] = id_element(name="SV3")

    MonetaryAmount: Optional[X12R] = element(
        name="SV302",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    FacilityCodeValue: Optional[X12AN] = element(
        name="SV303",
        description="Facility Code Value",
        min_length=1,
        max_length=2,
    )

    ProsthesisCrownOrInlayCode: Optional[X12ID] = element(
        name="SV305",
        description="Prosthesis, Crown or Inlay Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="SV306",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="SV307",
        description="Description",
        min_length=1,
        max_length=80,
    )

    CopayStatusCode: Optional[X12ID] = element(
        name="SV308",
        description="Copay Status Code",
        min_length=1,
        max_length=1,
    )

    ProviderAgreementCode: Optional[X12ID] = element(
        name="SV309",
        description="Provider Agreement Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SV310",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
