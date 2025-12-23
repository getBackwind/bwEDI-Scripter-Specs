# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class ER(Segment):
    """
    ER - Rail Event Reporting
    
    Description:
        To supply information regarding movement of shipments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ER/
    """
    _id: Literal["ER"] = id_element(name="ER")

    ActionCode: X12ID = element(
        name="ER01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="ER02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    EventCode: X12ID = element(
        name="ER03",
        description="Event Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    StandardPointLocationCode: X12ID = element(
        name="ER04",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    DateTimeQualifier: X12ID = element(
        name="ER05",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="ER06",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="ER07",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="ER08",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    InterchangeTrainIdentification: Optional[X12AN] = element(
        name="ER09",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )

    Date: Optional[X12DT] = element(
        name="ER10",
        description="Date",
        min_length=8,
        max_length=8,
    )

    LoadEmptyStatusCode: Optional[X12ID] = element(
        name="ER11",
        description="Load/Empty Status Code",
        min_length=1,
        max_length=1,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="ER12",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )
