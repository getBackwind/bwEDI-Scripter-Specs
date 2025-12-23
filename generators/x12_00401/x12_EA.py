# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class EA(Segment):
    """
    EA - Equipment Attributes
    
    Description:
        To specify attributes required for a piece of equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/EA/
    """
    _id: Literal["EA"] = id_element(name="EA")

    EquipmentAttributeCode: X12ID = element(
        name="EA01",
        description="Equipment Attribute Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="EA0201",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Exponent: Optional[X12R] = element(
        name="EA0202",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier: Optional[X12R] = element(
        name="EA0203",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="EA0204",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent2: Optional[X12R] = element(
        name="EA0205",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier2: Optional[X12R] = element(
        name="EA0206",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="EA0207",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent3: Optional[X12R] = element(
        name="EA0208",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier3: Optional[X12R] = element(
        name="EA0209",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="EA0210",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent4: Optional[X12R] = element(
        name="EA0211",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier4: Optional[X12R] = element(
        name="EA0212",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="EA0213",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent5: Optional[X12R] = element(
        name="EA0214",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier5: Optional[X12R] = element(
        name="EA0215",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    Quantity: Optional[X12R] = element(
        name="EA03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
