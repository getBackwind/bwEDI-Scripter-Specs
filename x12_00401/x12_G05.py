# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class G05(Segment):
    """
    G05 - Total Shipment Information
    
    Description:
        To provide totals relating to the shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G05/
    """
    _id: Literal["G05"] = id_element(name="G05")

    NumberOfUnitsShipped: Optional[X12R] = element(
        name="G0501",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G0502",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="G0503",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="G0504",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="G0505",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="G0506",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="G0507",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="G0508",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
