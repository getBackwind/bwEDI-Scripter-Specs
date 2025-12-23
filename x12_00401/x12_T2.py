# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class T2(Segment):
    """
    T2 - Transit Inbound Lading
    
    Description:
        To specify lading description, including weight and rate details applying to the associated T1 segment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/T2/
    """
    _id: Literal["T2"] = id_element(name="T2")

    AssignedNumber: X12Nn = element(
        name="T201",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    LadingDescription: Optional[X12AN] = element(
        name="T202",
        description="Lading Description",
        min_length=1,
        max_length=50,
    )

    Weight: Optional[X12R] = element(
        name="T203",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="T204",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    FreightRate: Optional[X12R] = element(
        name="T205",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="T206",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    FreightRate2: Optional[X12R] = element(
        name="T207",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="T208",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="T209",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    CityName2: Optional[X12AN] = element(
        name="T210",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    ThroughSurchargePercent: Optional[X12Nn] = element(
        name="T211",
        description="Through Surcharge Percent",
        min_length=2,
        max_length=4,
    )

    PaidInSurchargePercent: Optional[X12Nn] = element(
        name="T212",
        description="Paid-In Surcharge Percent",
        min_length=2,
        max_length=4,
    )
