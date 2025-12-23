# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SN1(Segment):
    """
    SN1 - Item Detail (Shipment)
    
    Description:
        To specify line-item detail relative to shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SN1/
    """
    _id: Literal["SN1"] = id_element(name="SN1")

    LineID: Optional[X12AN] = element(
        name="SN101",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    UnitsShippedCount: X12R = element(
        name="SN102",
        description="Number of Units Shipped",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    UOM: X12ID = element(
        name="SN103",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    QuantityShippedToDate: Optional[X12R] = element(
        name="SN104",
        description="Quantity Shipped to Date",
        min_length=1,
        max_length=15,
    )

    QuantityOrdered: Optional[X12R] = element(
        name="SN105",
        description="Quantity Ordered",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="SN106",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    ReturnableContainerLoadMakeUpCode: Optional[X12ID] = element(
        name="SN107",
        description="Returnable Container Load Make-Up Code",
        min_length=1,
        max_length=2,
    )

    LineItemStatusCode: Optional[X12ID] = element(
        name="SN108",
        description="Line Item Status Code",
        min_length=2,
        max_length=2,
    )
