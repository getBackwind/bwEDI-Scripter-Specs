# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class IV1(Segment):
    """
    IV1 - Lane Estimates
    
    Description:
        To identify data applicable to the lanes covered by this proposal
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IV1/
    """
    _id: Literal["IV1"] = id_element(name="IV1")

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="IV101",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="IV102",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    Number: Optional[X12Nn] = element(
        name="IV103",
        description="Number",
        min_length=1,
        max_length=9,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="IV104",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="IV105",
        description="Unit of Time Period or Interval",
    )
