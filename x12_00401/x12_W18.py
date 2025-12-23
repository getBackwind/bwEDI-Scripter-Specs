# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class W18(Segment):
    """
    W18 - Probe Temperatures
    
    Description:
        To indicate receipt temperature by location
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W18/
    """
    _id: Literal["W18"] = id_element(name="W18")

    TemperatureProbeLocationCode: X12ID = element(
        name="W1801",
        description="Temperature Probe Location Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Temperature: X12R = element(
        name="W1802",
        description="Temperature",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="W1803",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
