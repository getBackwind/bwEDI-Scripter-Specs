# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class CAL(Segment):
    """
    CAL - Calendar
    
    Description:
        To identify the calendar and working shift details for the plan or schedule
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CAL/
    """
    _id: Literal["CAL"] = id_element(name="CAL")

    ReferenceIdentificationQualifier: X12ID = element(
        name="CAL01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="CAL02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="CAL03",
        description="Unit of Time Period or Interval",
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="CAL04",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="CAL05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="CAL06",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="CAL07",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    ShipDeliveryOrCalendarPatternCode: Optional[X12ID] = element(
        name="CAL08",
        description="Ship/Delivery or Calendar Pattern Code",
        min_length=1,
        max_length=2,
    )

    DateTimeQualifier2: Optional[X12ID] = element(
        name="CAL09",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="CAL10",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="CAL11",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode2: Optional[X12ID] = element(
        name="CAL12",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    ShipDeliveryOrCalendarPatternCode2: Optional[X12ID] = element(
        name="CAL13",
        description="Ship/Delivery or Calendar Pattern Code",
        min_length=1,
        max_length=2,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="CAL14",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="CAL15",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="CAL16",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )
