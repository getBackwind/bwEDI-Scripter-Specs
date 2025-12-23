# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class PPD(Segment):
    """
    PPD - Payment Pattern Details
    
    Description:
        To identify the payment pattern of specific, credit-related items
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PPD/
    """
    _id: Literal["PPD"] = id_element(name="PPD")

    PaymentPattern: Optional[X12AN] = element(
        name="PPD01",
        description="Payment Pattern",
        min_length=1,
        max_length=84,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="PPD02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="PPD03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PPD04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="PPD05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    RatingCode: Optional[X12ID] = element(
        name="PPD06",
        description="Rating Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="PPD07",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Number: Optional[X12Nn] = element(
        name="PPD08",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number2: Optional[X12Nn] = element(
        name="PPD09",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number3: Optional[X12Nn] = element(
        name="PPD10",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number4: Optional[X12Nn] = element(
        name="PPD11",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number5: Optional[X12Nn] = element(
        name="PPD12",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number6: Optional[X12Nn] = element(
        name="PPD13",
        description="Number",
        min_length=1,
        max_length=9,
    )
