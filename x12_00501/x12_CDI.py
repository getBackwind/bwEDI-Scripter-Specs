# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class CDI(Segment):
    """
    CDI - Change Detail Information
    
    Description:
        To provide information on changes or adjustments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CDI/
    """
    _id: Literal["CDI"] = id_element(name="CDI")

    OptionTypeCode: Optional[X12ID] = element(
        name="CDI01",
        description="Option Type Code",
        min_length=1,
        max_length=2,
    )

    ConvertibilityRateTypeCode: Optional[X12ID] = element(
        name="CDI03",
        description="Convertibility Rate Type Code",
        min_length=1,
        max_length=2,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="CDI04",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="CDI05",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="CDI06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Number: Optional[X12Nn] = element(
        name="CDI07",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number2: Optional[X12Nn] = element(
        name="CDI08",
        description="Number",
        min_length=1,
        max_length=9,
    )

    IndexIdentityCode: Optional[X12ID] = element(
        name="CDI09",
        description="Index Identity Code",
        min_length=2,
        max_length=2,
    )

    PrimarySourceOfIndexCode: Optional[X12ID] = element(
        name="CDI10",
        description="Primary Source of Index Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="CDI11",
        description="Description",
        min_length=1,
        max_length=80,
    )
