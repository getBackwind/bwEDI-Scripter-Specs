# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ADX(Segment):
    """
    ADX - Adjustment
    
    Description:
        To convey accounts-payable adjustment information for the purpose of cash application, including payer-generated debit/credit memos
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ADX/
    """
    _id: Literal["ADX"] = id_element(name="ADX")

    MonetaryAmount: X12R = element(
        name="ADX01",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    AdjustmentReasonCode: X12ID = element(
        name="ADX02",
        description="Adjustment Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="ADX03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ADX04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
