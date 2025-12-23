# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class K3(Segment):
    """
    K3 - File Information
    
    Description:
        To transmit a fixed-format record or matrix contents
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/K3/
    """
    _id: Literal["K3"] = id_element(name="K3")

    FixedFormatInformation: X12AN = element(
        name="K301",
        description="Fixed Format Information",
        mandatory=True,
        min_length=1,
        max_length=80,
    )

    RecordFormatCode: Optional[X12ID] = element(
        name="K302",
        description="Record Format Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="K30301",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Exponent: Optional[X12R] = element(
        name="K30302",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier: Optional[X12R] = element(
        name="K30303",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="K30304",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent2: Optional[X12R] = element(
        name="K30305",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier2: Optional[X12R] = element(
        name="K30306",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="K30307",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent3: Optional[X12R] = element(
        name="K30308",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier3: Optional[X12R] = element(
        name="K30309",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="K30310",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent4: Optional[X12R] = element(
        name="K30311",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier4: Optional[X12R] = element(
        name="K30312",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="K30313",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent5: Optional[X12R] = element(
        name="K30314",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier5: Optional[X12R] = element(
        name="K30315",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )
