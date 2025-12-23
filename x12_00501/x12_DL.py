# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class DL(Segment):
    """
    DL - Auto Claim Detail - Labor
    
    Description:
        To describe the labor involved in the repair of vehicle damage and to specify actions taken related to the labor
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DL/
    """
    _id: Literal["DL"] = id_element(name="DL")

    ActionCode: X12ID = element(
        name="DL01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    LaborHours: Optional[X12Nn] = element(
        name="DL02",
        description="Labor Hours",
        min_length=1,
        max_length=3,
    )

    LaborHours2: Optional[X12Nn] = element(
        name="DL03",
        description="Labor Hours",
        min_length=1,
        max_length=3,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="DL04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Amount: Optional[X12Nn] = element(
        name="DL05",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Number: Optional[X12Nn] = element(
        name="DL06",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number2: Optional[X12Nn] = element(
        name="DL07",
        description="Number",
        min_length=1,
        max_length=9,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="DL08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="DL09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode4: Optional[X12ID] = element(
        name="DL10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode5: Optional[X12ID] = element(
        name="DL11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
