# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class OID(Segment):
    """
    OID - Order Identification Detail
    
    Description:
        To specify order identification detail
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/OID/
    """
    _id: Literal["OID"] = id_element(name="OID")

    ReferenceIdentification: Optional[X12AN] = element(
        name="OID01",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="OID02",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="OID03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="OID04",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="OID05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="OID06",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="OID07",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="OID08",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="OID09",
        description="Volume",
        min_length=1,
        max_length=8,
    )
