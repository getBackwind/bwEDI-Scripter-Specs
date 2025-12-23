# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class CYC(Segment):
    """
    CYC - Car Hire Cycle
    
    Description:
        To identify the car hire beginning and ending cycle location and associated information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CYC/
    """
    _id: Literal["CYC"] = id_element(name="CYC")

    Year: X12Nn = element(
        name="CYC01",
        description="Year",
        mandatory=True,
        min_length=4,
        max_length=4,
    )

    MonthOfTheYearCode: X12ID = element(
        name="CYC02",
        description="Month of the Year Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CycleMonthHours: X12Nn = element(
        name="CYC03",
        description="Cycle Month Hours",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    StandardPointLocationCode: X12ID = element(
        name="CYC04",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="CYC05",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    AssociationOfAmericanRailroadsAARPoolCode: Optional[X12ID] = element(
        name="CYC06",
        description="Association of American Railroads (AAR) Pool Code",
        min_length=7,
        max_length=7,
    )
