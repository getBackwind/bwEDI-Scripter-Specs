# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class RMT(Segment):
    """
    RMT - Remittance Advice
    
    Description:
        To indicate the detail on items
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RMT/
    """
    _id: Literal["RMT"] = id_element(name="RMT")

    ReferenceIdentificationQualifier: X12ID = element(
        name="RMT01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="RMT02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="RMT03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="RMT04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="RMT05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="RMT06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="RMT07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount6: Optional[X12R] = element(
        name="RMT08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    AdjustmentReasonCode: Optional[X12ID] = element(
        name="RMT09",
        description="Adjustment Reason Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="RMT10",
        description="Description",
        min_length=1,
        max_length=80,
    )
