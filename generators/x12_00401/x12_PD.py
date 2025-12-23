# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class PD(Segment):
    """
    PD - Pricing Data
    
    Description:
        To describe the pricing basic input detail
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PD/
    """
    _id: Literal["PD"] = id_element(name="PD")

    UnitOfTimePeriodOrInterval: X12ID = element(
        name="PD01",
        description="Unit of Time Period or Interval",
        mandatory=True,
    )

    Date: X12DT = element(
        name="PD02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="PD0301",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Exponent: Optional[X12R] = element(
        name="PD0302",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier: Optional[X12R] = element(
        name="PD0303",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="PD0304",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent2: Optional[X12R] = element(
        name="PD0305",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier2: Optional[X12R] = element(
        name="PD0306",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="PD0307",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent3: Optional[X12R] = element(
        name="PD0308",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier3: Optional[X12R] = element(
        name="PD0309",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="PD0310",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent4: Optional[X12R] = element(
        name="PD0311",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier4: Optional[X12R] = element(
        name="PD0312",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="PD0313",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Exponent5: Optional[X12R] = element(
        name="PD0314",
        description="Exponent",
        min_length=1,
        max_length=15,
    )

    Multiplier5: Optional[X12R] = element(
        name="PD0315",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    Quantity: X12R = element(
        name="PD04",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Name: X12AN = element(
        name="PD05",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    Description: Optional[X12AN] = element(
        name="PD06",
        description="Description",
        min_length=1,
        max_length=80,
    )

    BreakdownStructureDetailCode: Optional[X12ID] = element(
        name="PD07",
        description="Breakdown Structure Detail Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PD08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description2: Optional[X12AN] = element(
        name="PD09",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ProposalDataDetailIdentifierCode: Optional[X12ID] = element(
        name="PD10",
        description="Proposal Data Detail Identifier Code",
        min_length=2,
        max_length=2,
    )
