# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SLI(Segment):
    """
    SLI - Specific Loan Information
    
    Description:
        To provide information for the loan under consideration
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SLI/
    """
    _id: Literal["SLI"] = id_element(name="SLI")

    LoanTypeCode: X12ID = element(
        name="SLI01",
        description="Loan Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    MonetaryAmount: X12R = element(
        name="SLI02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: X12R = element(
        name="SLI03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    InterestRate: X12R = element(
        name="SLI04",
        description="Interest Rate",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    LoanRateTypeCode: X12ID = element(
        name="SLI05",
        description="Loan Rate Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="SLI06",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="SLI07",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="SLI08",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SLI09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="SLI10",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="SLI11",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriodFormatQualifier3: Optional[X12ID] = element(
        name="SLI12",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="SLI13",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="SLI14",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="SLI15",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="SLI16",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="SLI17",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SLI18",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="SLI19",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier4: Optional[X12ID] = element(
        name="SLI20",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod4: Optional[X12AN] = element(
        name="SLI21",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    PaymentMethodTypeCode: Optional[X12ID] = element(
        name="SLI22",
        description="Payment Method Type Code",
        min_length=1,
        max_length=2,
    )
