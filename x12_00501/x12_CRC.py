# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class CRC(Segment):
    """
    CRC - Conditions Indicator
    
    Description:
        To supply information on conditions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CRC/
    """
    _id: Literal["CRC"] = id_element(name="CRC")

    CodeCategory: X12ID = element(
        name="CRC01",
        description="Code Category",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="CRC02",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ConditionIndicator: X12ID = element(
        name="CRC03",
        description="Condition Indicator",
        mandatory=True,
    )

    ConditionIndicator2: Optional[X12ID] = element(
        name="CRC04",
        description="Condition Indicator",
    )

    ConditionIndicator3: Optional[X12ID] = element(
        name="CRC05",
        description="Condition Indicator",
    )

    ConditionIndicator4: Optional[X12ID] = element(
        name="CRC06",
        description="Condition Indicator",
    )

    ConditionIndicator5: Optional[X12ID] = element(
        name="CRC07",
        description="Condition Indicator",
    )
