# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ATN(Segment):
    """
    ATN - Attendance
    
    Description:
        To specify attendance information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ATN/
    """
    _id: Literal["ATN"] = id_element(name="ATN")

    Quantity: X12R = element(
        name="ATN01",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="ATN02",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="ATN03",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="ATN04",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    AttendanceTypeCode: Optional[X12ID] = element(
        name="ATN05",
        description="Attendance Type Code",
        min_length=1,
        max_length=4,
    )

    Description: Optional[X12AN] = element(
        name="ATN06",
        description="Description",
        min_length=1,
        max_length=80,
    )
