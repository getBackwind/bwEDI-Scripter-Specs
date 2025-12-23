# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class OBI(Segment):
    """
    OBI - Obligation Information
    
    Description:
        To identify borrower's financial obligation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/OBI/
    """
    _id: Literal["OBI"] = id_element(name="OBI")

    ObligationTypeCode: X12ID = element(
        name="OBI01",
        description="Obligation Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Name: Optional[X12AN] = element(
        name="OBI02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="OBI03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="OBI04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="OBI05",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="OBI06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
