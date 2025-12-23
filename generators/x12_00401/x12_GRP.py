# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn


class GRP(Segment):
    """
    GRP - Group Dosage Parameters
    
    Description:
        To report group-specific variables on dosages
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/GRP/
    """
    _id: Literal["GRP"] = id_element(name="GRP")

    Number: X12Nn = element(
        name="GRP01",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    UnitDoseCode: X12ID = element(
        name="GRP02",
        description="Unit Dose Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="GRP03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: X12DT = element(
        name="GRP04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )
