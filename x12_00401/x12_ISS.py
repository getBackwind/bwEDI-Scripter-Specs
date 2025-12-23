# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class ISS(Segment):
    """
    ISS - Invoice Shipment Summary
    
    Description:
        To specify summary details of total items shipped in terms of quantity, weight, and volume
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ISS/
    """
    _id: Literal["ISS"] = id_element(name="ISS")

    UnitsShipped: Optional[X12R] = element(
        name="ISS01",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    UomCode: Optional[X12ID] = element(
        name="ISS02",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="ISS03",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUomCode: Optional[X12ID] = element(
        name="ISS04",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="ISS05",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="ISS06",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="ISS07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Weight2: Optional[X12R] = element(
        name="ISS08",
        description="Weight",
        min_length=1,
        max_length=10,
    )
