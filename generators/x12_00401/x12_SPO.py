# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SPO(Segment):
    """
    SPO - Shipment Purchase Order Detail
    
    Description:
        To specify the purchase order details for a shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SPO/
    """
    _id: Literal["SPO"] = id_element(name="SPO")

    PurchaseOrderNumber: X12AN = element(
        name="SPO01",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="SPO02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="SPO03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="SPO04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="SPO05",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="SPO06",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    ApplicationErrorConditionCode: Optional[X12ID] = element(
        name="SPO07",
        description="Application Error Condition Code",
        min_length=1,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="SPO08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
