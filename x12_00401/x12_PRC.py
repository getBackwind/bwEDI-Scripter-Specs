# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PRC(Segment):
    """
    PRC - Payment Rate Change
    
    Description:
        To identify interest rate or payment changes for adjustable rate mortgages
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PRC/
    """
    _id: Literal["PRC"] = id_element(name="PRC")

    DateTimeQualifier: X12ID = element(
        name="PRC01",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="PRC02",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="PRC03",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    InterestRate: Optional[X12R] = element(
        name="PRC04",
        description="Interest Rate",
        min_length=1,
        max_length=6,
    )

    InterestRate2: Optional[X12R] = element(
        name="PRC05",
        description="Interest Rate",
        min_length=1,
        max_length=6,
    )

    InterestRate3: Optional[X12R] = element(
        name="PRC06",
        description="Interest Rate",
        min_length=1,
        max_length=6,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="PRC07",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PRC08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PRC09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="PRC10",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="PRC11",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
