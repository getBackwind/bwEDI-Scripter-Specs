# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class VRC(Segment):
    """
    VRC - Vehicle Recovery
    
    Description:
        To provide information about the recovery of a vehicle
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/VRC/
    """
    _id: Literal["VRC"] = id_element(name="VRC")

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="VRC01",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="VRC02",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Quantity: Optional[X12R] = element(
        name="VRC03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    RecoveryConditionCode: Optional[X12ID] = element(
        name="VRC04",
        description="Recovery Condition Code",
        min_length=1,
        max_length=1,
    )

    RecoveryClassificationCode: Optional[X12ID] = element(
        name="VRC05",
        description="Recovery Classification Code",
        min_length=1,
        max_length=1,
    )
