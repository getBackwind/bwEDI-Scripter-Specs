# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class FIR(Segment):
    """
    FIR - Financial Information
    
    Description:
        To specify the details of financial information transactions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FIR/
    """
    _id: Literal["FIR"] = id_element(name="FIR")

    CodeListQualifierCode: X12ID = element(
        name="FIR01",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="FIR02",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    MonetaryAmount: X12R = element(
        name="FIR03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Date: Optional[X12DT] = element(
        name="FIR04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="FIR05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="FIR06",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="FIR07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="FIR08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    CreditDebitFlagCode: Optional[X12ID] = element(
        name="FIR09",
        description="Credit/Debit Flag Code",
        min_length=1,
        max_length=1,
    )

    FinancialTransactionStatusCode: Optional[X12ID] = element(
        name="FIR10",
        description="Financial Transaction Status Code",
        min_length=1,
        max_length=2,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="FIR11",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="FIR12",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
