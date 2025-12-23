# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class G29(Segment):
    """
    G29 - Store Display Information
    
    Description:
        To specify product display information for a retail store
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G29/
    """
    _id: Literal["G29"] = id_element(name="G29")

    DisplayTypeCode: X12ID = element(
        name="G2901",
        description="Display Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="G2902",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G2903",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
