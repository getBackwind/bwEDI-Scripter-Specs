# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ICM(Segment):
    """
    ICM - Individual Income
    
    Description:
        To supply information to determine benefit eligibility, deductibles, and retirement and investment contributions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ICM/
    """
    _id: Literal["ICM"] = id_element(name="ICM")

    FrequencyCode: X12ID = element(
        name="ICM01",
        description="Frequency Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    MonetaryAmount: X12R = element(
        name="ICM02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="ICM03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="ICM04",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    SalaryGrade: Optional[X12AN] = element(
        name="ICM05",
        description="Salary Grade",
        min_length=1,
        max_length=5,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="ICM06",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
