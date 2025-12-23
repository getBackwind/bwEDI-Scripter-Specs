# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CR3(Segment):
    """
    CR3 - Durable Medical Equipment Certification
    
    Description:
        To supply information regarding a physician's certification for durable medical equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CR3/
    """
    _id: Literal["CR3"] = id_element(name="CR3")

    CertificationTypeCode: Optional[X12ID] = element(
        name="CR301",
        description="Certification Type Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="CR302",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="CR303",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    InsulinDependentCode: Optional[X12ID] = element(
        name="CR304",
        description="Insulin Dependent Code",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="CR305",
        description="Description",
        min_length=1,
        max_length=80,
    )
