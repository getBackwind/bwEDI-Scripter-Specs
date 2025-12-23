# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class G23(Segment):
    """
    G23 - Terms of Sale
    
    Description:
        To specify the terms of sale
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G23/
    """
    _id: Literal["G23"] = id_element(name="G23")

    TermsTypeCode: X12ID = element(
        name="G2301",
        description="Terms Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TermsBasisDateCode: X12ID = element(
        name="G2302",
        description="Terms Basis Date Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    TermsStartDate: Optional[X12DT] = element(
        name="G2303",
        description="Terms Start Date",
        min_length=8,
        max_length=8,
    )

    TermsDueDateQualifier: Optional[X12ID] = element(
        name="G2304",
        description="Terms Due Date Qualifier",
        min_length=2,
        max_length=2,
    )

    TermsDiscountPercent: Optional[X12R] = element(
        name="G2305",
        description="Terms Discount Percent",
        min_length=1,
        max_length=6,
    )

    TermsDiscountDueDate: Optional[X12DT] = element(
        name="G2306",
        description="Terms Discount Due Date",
        min_length=8,
        max_length=8,
    )

    TermsDiscountDaysDue: Optional[X12Nn] = element(
        name="G2307",
        description="Terms Discount Days Due",
        min_length=1,
        max_length=3,
    )

    TermsNetDueDate: Optional[X12DT] = element(
        name="G2308",
        description="Terms Net Due Date",
        min_length=8,
        max_length=8,
    )

    TermsNetDays: Optional[X12Nn] = element(
        name="G2309",
        description="Terms Net Days",
        min_length=1,
        max_length=3,
    )

    TermsDiscountAmount: Optional[X12Nn] = element(
        name="G2310",
        description="Terms Discount Amount",
        min_length=1,
        max_length=10,
    )

    DiscountedAmountDue: Optional[X12Nn] = element(
        name="G2311",
        description="Discounted Amount Due",
        min_length=1,
        max_length=10,
    )

    AmountSubjectToTermsDiscount: Optional[X12Nn] = element(
        name="G2312",
        description="Amount Subject to Terms Discount",
        min_length=1,
        max_length=10,
    )

    InstallmentTotalInvoiceAmountDue: Optional[X12Nn] = element(
        name="G2313",
        description="Installment Total Invoice Amount Due",
        min_length=1,
        max_length=10,
    )

    PercentOfInvoicePayable: Optional[X12R] = element(
        name="G2314",
        description="Percent of Invoice Payable",
        min_length=1,
        max_length=5,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="G2315",
        description="Free-form Message",
        min_length=1,
        max_length=60,
    )

    InstallmentGroupIndicator: Optional[X12Nn] = element(
        name="G2316",
        description="Installment Group Indicator",
        min_length=2,
        max_length=2,
    )
