# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class ITD(Segment):
    """
    ITD - Terms of Sale/Deferred Terms of Sale
    
    Description:
        To specify terms of sale
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ITD/
    """
    _id: Literal["ITD"] = id_element(name="ITD")

    TypeCode: Optional[X12ID] = element(
        name="ITD01",
        description="Terms Type Code",
        min_length=2,
        max_length=2,
    )

    BasisDateCode: Optional[X12ID] = element(
        name="ITD02",
        description="Terms Basis Date Code",
        min_length=1,
        max_length=2,
    )

    DiscountCode: Optional[X12R] = element(
        name="ITD03",
        description="Terms Discount Percent",
        min_length=1,
        max_length=6,
    )

    DiscountDueDate: Optional[X12DT] = element(
        name="ITD04",
        description="Terms Discount Due Date",
        min_length=8,
        max_length=8,
    )

    DiscountDaysDue: Optional[X12Nn] = element(
        name="ITD05",
        description="Terms Discount Days Due",
        min_length=1,
        max_length=3,
    )

    NetDueDate: Optional[X12DT] = element(
        name="ITD06",
        description="Terms Net Due Date",
        min_length=8,
        max_length=8,
    )

    NetDays: Optional[X12Nn] = element(
        name="ITD07",
        description="Terms Net Days",
        min_length=1,
        max_length=3,
    )

    TermsDiscountAmount: Optional[X12Nn] = element(
        name="ITD08",
        description="Terms Discount Amount",
        min_length=1,
        max_length=10,
    )

    TermsDeferredDueDate: Optional[X12DT] = element(
        name="ITD09",
        description="Terms Deferred Due Date",
        min_length=8,
        max_length=8,
    )

    DeferredAmountDue: Optional[X12Nn] = element(
        name="ITD10",
        description="Deferred Amount Due",
        min_length=1,
        max_length=10,
    )

    PercentOfInvoicePayable: Optional[X12R] = element(
        name="ITD11",
        description="Percent of Invoice Payable",
        min_length=1,
        max_length=5,
    )

    Description: Optional[X12AN] = element(
        name="ITD12",
        description="Description",
        min_length=1,
        max_length=80,
    )

    DayOfMonth: Optional[X12Nn] = element(
        name="ITD13",
        description="Day of Month",
        min_length=1,
        max_length=2,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="ITD14",
        description="Payment Method Code",
    )

    Percent: Optional[X12R] = element(
        name="ITD15",
        description="Percent",
        min_length=1,
        max_length=10,
    )
