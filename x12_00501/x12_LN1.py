# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LN1(Segment):
    """
    LN1 - Loan Specific Data
    
    Description:
        To provide high-level information about a loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LN1/
    """
    _id: Literal["LN1"] = id_element(name="LN1")

    MonetaryAmount: X12R = element(
        name="LN101",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    LienPriorityCode: X12ID = element(
        name="LN102",
        description="Lien Priority Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RealEstateLoanTypeCode: X12ID = element(
        name="LN103",
        description="Real Estate Loan Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="LN104",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="LN105",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    PercentageAsDecimal2: Optional[X12R] = element(
        name="LN106",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="LN107",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="LN108",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    RealEstateLoanSecurityInstrumentCode: Optional[X12ID] = element(
        name="LN109",
        description="Real Estate Loan Security Instrument Code",
        min_length=1,
        max_length=1,
    )

    LoanDocumentationTypeCode: Optional[X12ID] = element(
        name="LN110",
        description="Loan Documentation Type Code",
        min_length=1,
        max_length=1,
    )

    LoanRateTypeCode: Optional[X12ID] = element(
        name="LN111",
        description="Loan Rate Type Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="LN112",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    AccountNumber: Optional[X12AN] = element(
        name="LN113",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    PercentageAsDecimal3: Optional[X12R] = element(
        name="LN114",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    PercentageAsDecimal4: Optional[X12R] = element(
        name="LN115",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="LN116",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="LN117",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="LN118",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="LN119",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod4: Optional[X12AN] = element(
        name="LN120",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod5: Optional[X12AN] = element(
        name="LN121",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="LN122",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="LN123",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
