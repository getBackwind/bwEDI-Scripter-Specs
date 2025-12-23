# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class SRT(Segment):
    """
    SRT - Scale Rate Header
    
    Description:
        To indicate the route code and indicate the rate/value qualifier, which define the use of other scale rate segments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SRT/
    """
    _id: Literal["SRT"] = id_element(name="SRT")

    ChangeTypeCode: X12ID = element(
        name="SRT01",
        description="Change Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RouteCode: Optional[X12AN] = element(
        name="SRT02",
        description="Route Code",
        min_length=1,
        max_length=13,
    )

    RateValueQualifier: X12ID = element(
        name="SRT03",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="SRT04",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    RateApplicationTypeCode: Optional[X12ID] = element(
        name="SRT05",
        description="Rate Application Type Code",
        min_length=1,
        max_length=1,
    )

    Scale: Optional[X12AN] = element(
        name="SRT06",
        description="Scale",
        min_length=1,
        max_length=10,
    )

    Scale2: Optional[X12AN] = element(
        name="SRT07",
        description="Scale",
        min_length=1,
        max_length=10,
    )

    MinimumWeightLogic: Optional[X12AN] = element(
        name="SRT08",
        description="Minimum/Weight Logic",
        min_length=1,
        max_length=2,
    )

    LoadingRestriction: Optional[X12Nn] = element(
        name="SRT09",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction2: Optional[X12Nn] = element(
        name="SRT10",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    Percent: Optional[X12Nn] = element(
        name="SRT11",
        description="Percent",
        min_length=1,
        max_length=3,
    )

    SpecialChargeOrAllowanceCode: Optional[X12ID] = element(
        name="SRT12",
        description="Special Charge or Allowance Code",
        min_length=3,
        max_length=3,
    )

    SpecialChargeDescription: Optional[X12AN] = element(
        name="SRT13",
        description="Special Charge Description",
        min_length=2,
        max_length=25,
    )
