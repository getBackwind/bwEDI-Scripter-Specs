# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SRD(Segment):
    """
    SRD - Scale Rate Detail
    
    Description:
        To specify the rate base, rates, and maximum miles in the scale tables
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SRD/
    """
    _id: Literal["SRD"] = id_element(name="SRD")

    DistanceQualifier: X12ID = element(
        name="SRD01",
        description="Distance Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RateBasisNumber: X12AN = element(
        name="SRD02",
        description="Rate Basis Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    DistanceQualifier2: Optional[X12ID] = element(
        name="SRD03",
        description="Distance Qualifier",
        min_length=1,
        max_length=1,
    )

    RateBasisNumber2: Optional[X12AN] = element(
        name="SRD04",
        description="Rate Basis Number",
        min_length=1,
        max_length=6,
    )

    FreightRate: X12R = element(
        name="SRD05",
        description="Freight Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    FreightRate2: Optional[X12R] = element(
        name="SRD06",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate3: Optional[X12R] = element(
        name="SRD07",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate4: Optional[X12R] = element(
        name="SRD08",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate5: Optional[X12R] = element(
        name="SRD09",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate6: Optional[X12R] = element(
        name="SRD10",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate7: Optional[X12R] = element(
        name="SRD11",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate8: Optional[X12R] = element(
        name="SRD12",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate9: Optional[X12R] = element(
        name="SRD13",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate10: Optional[X12R] = element(
        name="SRD14",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate11: Optional[X12R] = element(
        name="SRD15",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate12: Optional[X12R] = element(
        name="SRD16",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate13: Optional[X12R] = element(
        name="SRD17",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate14: Optional[X12R] = element(
        name="SRD18",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate15: Optional[X12R] = element(
        name="SRD19",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate16: Optional[X12R] = element(
        name="SRD20",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )
