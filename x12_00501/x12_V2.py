# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class V2(Segment):
    """
    V2 - Vessel Information
    
    Description:
        To provide vessel details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/V2/
    """
    _id: Literal["V2"] = id_element(name="V2")

    LocationIdentifier: Optional[X12AN] = element(
        name="V201",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="V202",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Weight: Optional[X12R] = element(
        name="V203",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="V204",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight2: Optional[X12R] = element(
        name="V205",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode2: Optional[X12ID] = element(
        name="V206",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight3: Optional[X12R] = element(
        name="V207",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode3: Optional[X12ID] = element(
        name="V208",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight4: Optional[X12R] = element(
        name="V209",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode4: Optional[X12ID] = element(
        name="V210",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight5: Optional[X12R] = element(
        name="V211",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode5: Optional[X12ID] = element(
        name="V212",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Name: Optional[X12AN] = element(
        name="V213",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Length: Optional[X12R] = element(
        name="V214",
        description="Length",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="V215",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="V216",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="V217",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
