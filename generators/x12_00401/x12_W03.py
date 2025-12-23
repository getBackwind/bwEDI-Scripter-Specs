# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class W03(Segment):
    """
    W03 - Total Shipment Information
    
    Description:
        To provide totals relating to the shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W03/
    """
    _id: Literal["W03"] = id_element(name="W03")

    NumberOfUnitsShipped: X12R = element(
        name="W0301",
        description="Number of Units Shipped",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    Weight: Optional[X12R] = element(
        name="W0302",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="W0303",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="W0304",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="W0305",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="W0306",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="W0307",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
