# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class TLN(Segment):
    """
    TLN - Tradeline
    
    Description:
        To report specific details on a tradeline or credit-related item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TLN/
    """
    _id: Literal["TLN"] = id_element(name="TLN")

    AccountNumber: X12AN = element(
        name="TLN01",
        description="Account Number",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="TLN02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="TLN03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    TypeOfAccountCode: Optional[X12ID] = element(
        name="TLN04",
        description="Type of Account Code",
        min_length=2,
        max_length=2,
    )

    TypeOfAccountCode2: Optional[X12ID] = element(
        name="TLN05",
        description="Type of Account Code",
        min_length=2,
        max_length=2,
    )

    TypeOfCreditAccountCode: Optional[X12ID] = element(
        name="TLN06",
        description="Type of Credit Account Code",
        min_length=1,
        max_length=1,
    )

    Number: Optional[X12Nn] = element(
        name="TLN07",
        description="Number",
        min_length=1,
        max_length=9,
    )

    LoanTypeCode: Optional[X12ID] = element(
        name="TLN08",
        description="Loan Type Code",
        min_length=1,
        max_length=2,
    )

    RatingCode: Optional[X12ID] = element(
        name="TLN09",
        description="Rating Code",
        min_length=2,
        max_length=2,
    )

    RatingRemarksCode: Optional[X12ID] = element(
        name="TLN10",
        description="Rating Remarks Code",
        min_length=2,
        max_length=2,
    )

    SourceOfDisclosureCode: Optional[X12ID] = element(
        name="TLN11",
        description="Source of Disclosure Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="TLN12",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="TLN13",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="TLN14",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    RatingCode2: Optional[X12ID] = element(
        name="TLN15",
        description="Rating Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="TLN16",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="TLN17",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="TLN18",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    RatingCode3: Optional[X12ID] = element(
        name="TLN19",
        description="Rating Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="TLN20",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Number2: Optional[X12Nn] = element(
        name="TLN21",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Description: Optional[X12AN] = element(
        name="TLN22",
        description="Description",
        min_length=1,
        max_length=80,
    )
