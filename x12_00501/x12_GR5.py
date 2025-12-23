# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class GR5(Segment):
    """
    GR5 - Loading Details
    
    Description:
        To provide loading details for equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/GR5/
    """
    _id: Literal["GR5"] = id_element(name="GR5")

    SpecialHandlingCode: X12ID = element(
        name="GR501",
        description="Special Handling Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    SurfaceLayerPositionCode: Optional[X12ID] = element(
        name="GR502",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )

    MeasurementValue: Optional[X12R] = element(
        name="GR503",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="GR504",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="GR505",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )
