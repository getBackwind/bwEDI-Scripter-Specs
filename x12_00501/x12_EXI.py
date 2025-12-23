# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class EXI(Segment):
    """
    EXI - Excavation Ticket Information
    
    Description:
        To supply excavation ticket information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EXI/
    """
    _id: Literal["EXI"] = id_element(name="EXI")

    Priority: X12Nn = element(
        name="EXI02",
        description="Priority",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="EXI03",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="EXI04",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    TimePeriodUnitQualifier: Optional[X12ID] = element(
        name="EXI05",
        description="Time Period Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="EXI06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="EXI07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ActionCode: Optional[X12ID] = element(
        name="EXI08",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
