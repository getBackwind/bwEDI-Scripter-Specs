# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PYD(Segment):
    """
    PYD - Payroll Deduction
    
    Description:
        To specify payroll deduction information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PYD/
    """
    _id: Literal["PYD"] = id_element(name="PYD")

    MonetaryAmount: X12R = element(
        name="PYD01",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="PYD02",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    TaxTreatmentCode: Optional[X12ID] = element(
        name="PYD03",
        description="Tax Treatment Code",
        min_length=1,
        max_length=1,
    )

    DeductionTypeCode: Optional[X12ID] = element(
        name="PYD04",
        description="Deduction Type Code",
        min_length=1,
        max_length=4,
    )

    Description: Optional[X12AN] = element(
        name="PYD05",
        description="Description",
        min_length=1,
        max_length=80,
    )
