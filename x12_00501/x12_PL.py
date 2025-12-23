# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class PL(Segment):
    """
    PL - Proposal Cost Logic
    
    Description:
        To describe the cost logic used when pricing a particular aspect of a proposal
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PL/
    """
    _id: Literal["PL"] = id_element(name="PL")

    AssignedNumber: X12Nn = element(
        name="PL01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="PL0201",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Exponent: Optional[X12R] = element(
        name="PL0202",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier: Optional[X12R] = element(
        name="PL0203",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="PL0204",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent2: Optional[X12R] = element(
        name="PL0205",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier2: Optional[X12R] = element(
        name="PL0206",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="PL0207",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent3: Optional[X12R] = element(
        name="PL0208",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier3: Optional[X12R] = element(
        name="PL0209",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="PL0210",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent4: Optional[X12R] = element(
        name="PL0211",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier4: Optional[X12R] = element(
        name="PL0212",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="PL0213",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent5: Optional[X12R] = element(
        name="PL0214",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier5: Optional[X12R] = element(
        name="PL0215",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    Name: X12AN = element(
        name="PL03",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    CalculationOperationCode: X12ID = element(
        name="PL04",
        description="Calculation Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="PL05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Count: Optional[X12Nn] = element(
        name="PL06",
        description="Count",
        min_length=1,
        max_length=9,
    )
