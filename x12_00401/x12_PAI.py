# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn, X12R


class PAI(Segment):
    """
    PAI - Print Advertisement Information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PAI/
    """
    _id: Literal["PAI"] = id_element(name="PAI")

    Date: Optional[X12DT] = element(
        name="PAI01",
        description="Date",
        min_length=8,
        max_length=8,
    )

    MeasurementValue: Optional[X12R] = element(
        name="PAI02",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="PAI03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="PAI04",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount2: Optional[X12Nn] = element(
        name="PAI05",
        description="Amount",
        min_length=1,
        max_length=15,
    )
