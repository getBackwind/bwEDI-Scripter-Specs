# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class LRQ(Segment):
    """
    LRQ - Mortgage Characteristics Requested
    
    Description:
        To describe the characteristics of a mortgage requested by the applicant(s)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LRQ/
    """
    _id: Literal["LRQ"] = id_element(name="LRQ")

    MonetaryAmount: X12R = element(
        name="LRQ01",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="LRQ02",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="LRQ03",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="LRQ04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    TypeOfResidenceCode: Optional[X12ID] = element(
        name="LRQ05",
        description="Type of Residence Code",
        min_length=1,
        max_length=1,
    )

    ContactMethodCode: Optional[X12ID] = element(
        name="LRQ06",
        description="Contact Method Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="LRQ07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    AssumptionTermsCode: Optional[X12ID] = element(
        name="LRQ08",
        description="Assumption Terms Code",
        min_length=1,
        max_length=1,
    )

    LoanPurposeCode: Optional[X12ID] = element(
        name="LRQ09",
        description="Loan Purpose Code",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="LRQ11",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="LRQ12",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Description: Optional[X12AN] = element(
        name="LRQ13",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description2: Optional[X12AN] = element(
        name="LRQ14",
        description="Description",
        min_length=1,
        max_length=80,
    )

    RealEstateLoanTypeCode: Optional[X12ID] = element(
        name="LRQ15",
        description="Real Estate Loan Type Code",
        min_length=1,
        max_length=1,
    )

    Description3: Optional[X12AN] = element(
        name="LRQ16",
        description="Description",
        min_length=1,
        max_length=80,
    )

    LoanPaymentTypeCode: Optional[X12ID] = element(
        name="LRQ17",
        description="Loan Payment Type Code",
        min_length=2,
        max_length=2,
    )

    Description4: Optional[X12AN] = element(
        name="LRQ18",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Number: Optional[X12Nn] = element(
        name="LRQ19",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Description5: Optional[X12AN] = element(
        name="LRQ20",
        description="Description",
        min_length=1,
        max_length=80,
    )

    CodeCategory: Optional[X12ID] = element(
        name="LRQ21",
        description="Code Category",
        min_length=2,
        max_length=2,
    )
