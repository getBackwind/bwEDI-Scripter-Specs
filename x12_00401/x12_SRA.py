# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class SRA(Segment):
    """
    SRA - Traffic Evaluation Factors
    
    Description:
        To specify factors used to generate and/or evaluate transportation rates and charges
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SRA/
    """
    _id: Literal["SRA"] = id_element(name="SRA")

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="SRA01",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MeasurementValue: X12R = element(
        name="SRA02",
        description="Measurement Value",
        mandatory=True,
        min_length=1,
        max_length=20,
    )
