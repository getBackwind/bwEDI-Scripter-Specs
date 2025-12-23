# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class SV(Segment):
    """
    SV - Service Description
    
    Description:
        To transmit the services standards and related service information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SV/
    """
    _id: Literal["SV"] = id_element(name="SV")

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="SV01",
        description="Unit of Time Period or Interval",
    )

    ServiceStandard: Optional[X12Nn] = element(
        name="SV02",
        description="Service Standard",
        min_length=1,
        max_length=4,
    )

    ServiceStandard2: Optional[X12Nn] = element(
        name="SV03",
        description="Service Standard",
        min_length=1,
        max_length=4,
    )

    TypeOfServiceOfferedCode: Optional[X12ID] = element(
        name="SV04",
        description="Type of Service Offered Code",
        min_length=1,
        max_length=1,
    )
