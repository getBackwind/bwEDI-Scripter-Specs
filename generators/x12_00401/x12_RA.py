# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class RA(Segment):
    """
    RA - Rate Header
    
    Description:
        To indicate a route code and other codes which define the use of the RB and FK segments which follow
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RA/
    """
    _id: Literal["RA"] = id_element(name="RA")

    RouteCode: X12AN = element(
        name="RA01",
        description="Route Code",
        mandatory=True,
        min_length=1,
        max_length=13,
    )

    RateValueQualifier: X12ID = element(
        name="RA02",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="RA03",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    AlternationPrecedenceCode: Optional[X12ID] = element(
        name="RA04",
        description="Alternation Precedence Code",
        min_length=1,
        max_length=1,
    )

    NumberOfRates: Optional[X12Nn] = element(
        name="RA05",
        description="Number of Rates",
        min_length=1,
        max_length=1,
    )

    UnitConversionFactor: Optional[X12Nn] = element(
        name="RA06",
        description="Unit Conversion Factor",
        min_length=1,
        max_length=9,
    )

    RateLevelQualifierCode: Optional[X12ID] = element(
        name="RA07",
        description="Rate Level Qualifier Code",
        min_length=1,
        max_length=1,
    )

    RateLevel: Optional[X12AN] = element(
        name="RA08",
        description="Rate Level",
        min_length=1,
        max_length=5,
    )

    Date: Optional[X12DT] = element(
        name="RA09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="RA10",
        description="Date",
        min_length=8,
        max_length=8,
    )
