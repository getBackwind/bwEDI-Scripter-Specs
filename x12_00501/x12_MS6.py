# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class MS6(Segment):
    """
    MS6 - Shipment Quantity and Weight
    
    Description:
        To specify shipment weight
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MS6/
    """
    _id: Literal["MS6"] = id_element(name="MS6")

    Quantity: X12R = element(
        name="MS601",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="MS602",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="MS603",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="MS604",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
