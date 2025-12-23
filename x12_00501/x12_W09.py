# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class W09(Segment):
    """
    W09 - Equipment and Temperature
    
    Description:
        To relate equipment type and required temperatures
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W09/
    """
    _id: Literal["W09"] = id_element(name="W09")

    EquipmentDescriptionCode: X12ID = element(
        name="W0901",
        description="Equipment Description Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Temperature: Optional[X12R] = element(
        name="W0902",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="W0903",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Temperature2: Optional[X12R] = element(
        name="W0904",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="W0905",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="W0906",
        description="Free-form Message",
        min_length=1,
        max_length=60,
    )

    VentSettingCode: Optional[X12ID] = element(
        name="W0907",
        description="Vent Setting Code",
        min_length=1,
        max_length=1,
    )

    PercentIntegerFormat: Optional[X12Nn] = element(
        name="W0908",
        description="Percent, Integer Format",
        min_length=1,
        max_length=3,
    )

    Quantity: Optional[X12R] = element(
        name="W0909",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
