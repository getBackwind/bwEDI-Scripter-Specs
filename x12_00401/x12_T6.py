# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class T6(Segment):
    """
    T6 - Transit Inbound Rates
    
    Description:
        To identify the transit inbound prior origin point and waybill reference of movement to the point specified in T1 segment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/T6/
    """
    _id: Literal["T6"] = id_element(name="T6")

    AssignedNumber: X12Nn = element(
        name="T601",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    FreightRate: Optional[X12R] = element(
        name="T602",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="T603",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="T604",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    FreightRate2: Optional[X12R] = element(
        name="T605",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="T606",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    CityName2: Optional[X12AN] = element(
        name="T607",
        description="City Name",
        min_length=2,
        max_length=30,
    )
