# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class FAA(Segment):
    """
    FAA - Financial Asset Account
    
    Description:
        To provide duration or amount of financial assets
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FAA/
    """
    _id: Literal["FAA"] = id_element(name="FAA")

    AccountNumberQualifier: X12ID = element(
        name="FAA01",
        description="Account Number Qualifier",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    AccountNumber: Optional[X12AN] = element(
        name="FAA02",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    Date: Optional[X12DT] = element(
        name="FAA03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="FAA04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    TypeOfAccountCode: Optional[X12ID] = element(
        name="FAA05",
        description="Type of Account Code",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="FAA06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="FAA08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="FAA09",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="FAA10",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="FAA11",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="FAA12",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="FAA13",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="FAA14",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
