# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class RCD(Segment):
    """
    RCD - Receiving Conditions
    
    Description:
        To report receiving conditions and specify contested quantities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RCD/
    """
    _id: Literal["RCD"] = id_element(name="RCD")

    AssignedIdentification: Optional[X12AN] = element(
        name="RCD01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    QuantityUnitsReceivedOrAccepted: Optional[X12R] = element(
        name="RCD02",
        description="Quantity Units Received or Accepted",
        min_length=1,
        max_length=9,
    )

    QuantityUnitsReturned: Optional[X12R] = element(
        name="RCD04",
        description="Quantity Units Returned",
        min_length=1,
        max_length=9,
    )

    QuantityInQuestion: Optional[X12R] = element(
        name="RCD06",
        description="Quantity in Question",
        min_length=1,
        max_length=9,
    )

    ReceivingConditionCode: Optional[X12ID] = element(
        name="RCD08",
        description="Receiving Condition Code",
        min_length=2,
        max_length=2,
    )

    QuantityInQuestion2: Optional[X12R] = element(
        name="RCD09",
        description="Quantity in Question",
        min_length=1,
        max_length=9,
    )

    ReceivingConditionCode2: Optional[X12ID] = element(
        name="RCD11",
        description="Receiving Condition Code",
        min_length=2,
        max_length=2,
    )

    QuantityInQuestion3: Optional[X12R] = element(
        name="RCD12",
        description="Quantity in Question",
        min_length=1,
        max_length=9,
    )

    ReceivingConditionCode3: Optional[X12ID] = element(
        name="RCD14",
        description="Receiving Condition Code",
        min_length=2,
        max_length=2,
    )

    QuantityInQuestion4: Optional[X12R] = element(
        name="RCD15",
        description="Quantity in Question",
        min_length=1,
        max_length=9,
    )

    ReceivingConditionCode4: Optional[X12ID] = element(
        name="RCD17",
        description="Receiving Condition Code",
        min_length=2,
        max_length=2,
    )

    QuantityInQuestion5: Optional[X12R] = element(
        name="RCD18",
        description="Quantity in Question",
        min_length=1,
        max_length=9,
    )

    ReceivingConditionCode5: Optional[X12ID] = element(
        name="RCD20",
        description="Receiving Condition Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="RCD21",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
