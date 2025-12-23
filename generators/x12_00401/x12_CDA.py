# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CDA(Segment):
    """
    CDA - Consumer Credit Account
    
    Description:
        To provide duration or amount of consumer credit account
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CDA/
    """
    _id: Literal["CDA"] = id_element(name="CDA")

    AccountNumber: Optional[X12AN] = element(
        name="CDA01",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="CDA02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="CDA03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="CDA04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="CDA05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    TypeOfAccountCode: Optional[X12ID] = element(
        name="CDA06",
        description="Type of Account Code",
        min_length=2,
        max_length=2,
    )

    TypeOfCreditAccountCode: Optional[X12ID] = element(
        name="CDA07",
        description="Type of Credit Account Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="CDA08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="CDA09",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="CDA10",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="CDA11",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="CDA12",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="CDA13",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod4: Optional[X12AN] = element(
        name="CDA14",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod5: Optional[X12AN] = element(
        name="CDA15",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Description: Optional[X12AN] = element(
        name="CDA16",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CDA17",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    LoanTypeCode: Optional[X12ID] = element(
        name="CDA18",
        description="Loan Type Code",
        min_length=1,
        max_length=2,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="CDA19",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="CDA20",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
