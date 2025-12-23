# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class RMR(Segment):
    """
    RMR - Remittance Advice Accounts Receivable Open Item Reference
    
    Description:
        To specify the accounts receivable open item(s) to be included in the cash application and to convey the appropriate detail
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RMR/
    """
    _id: Literal["RMR"] = id_element(name="RMR")

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="RMR01",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="RMR02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    PaymentActionCode: Optional[X12ID] = element(
        name="RMR03",
        description="Payment Action Code",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="RMR04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="RMR05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="RMR06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    AdjustmentReasonCode: Optional[X12ID] = element(
        name="RMR07",
        description="Adjustment Reason Code",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="RMR08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
