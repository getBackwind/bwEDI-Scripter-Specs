# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12TM


class ISC(Segment):
    """
    ISC - Interline Service Commitment Detail
    
    Description:
        To identify the service commitment schedules
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ISC/
    """
    _id: Literal["ISC"] = id_element(name="ISC")

    StandardCarrierAlphaCode: X12ID = element(
        name="ISC01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardPointLocationCode: X12ID = element(
        name="ISC02",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    EventCode: X12ID = element(
        name="ISC03",
        description="Event Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="ISC04",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="ISC05",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Time: Optional[X12TM] = element(
        name="ISC06",
        description="Time",
        min_length=4,
        max_length=8,
    )

    NumberOfDays: Optional[X12Nn] = element(
        name="ISC07",
        description="Number of Days",
        min_length=1,
        max_length=3,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="ISC08",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    InterchangeTrainIdentification: Optional[X12AN] = element(
        name="ISC09",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )

    BlockIdentifier: Optional[X12AN] = element(
        name="ISC10",
        description="Block Identifier",
        min_length=1,
        max_length=12,
    )
