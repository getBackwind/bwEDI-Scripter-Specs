# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R, X12TM


class PAM(Segment):
    """
    PAM - Period Amount
    
    Description:
        To indicate a quantity, and/or amount for an identified period
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PAM/
    """
    _id: Literal["PAM"] = id_element(name="PAM")

    QuantityQualifier: Optional[X12ID] = element(
        name="PAM01",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="PAM02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="PAM04",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PAM05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="PAM06",
        description="Unit of Time Period or Interval",
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="PAM07",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="PAM08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="PAM09",
        description="Time",
        min_length=4,
        max_length=8,
    )

    DateTimeQualifier2: Optional[X12ID] = element(
        name="PAM10",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="PAM11",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="PAM12",
        description="Time",
        min_length=4,
        max_length=8,
    )

    PercentQualifier: Optional[X12ID] = element(
        name="PAM13",
        description="Percent Qualifier",
        min_length=1,
        max_length=2,
    )

    Percent: Optional[X12R] = element(
        name="PAM14",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PAM15",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
