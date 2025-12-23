# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class R13(Segment):
    """
    R13 - Line Item Repair
    
    Description:
        To provide line item details of the equipment repair
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R13/
    """
    _id: Literal["R13"] = id_element(name="R13")

    AssignedIdentification: X12AN = element(
        name="R1301",
        description="Assigned Identification",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    IndustryCode: X12AN = element(
        name="R1302",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    IndustryCode2: X12AN = element(
        name="R1303",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    IndustryCode3: X12AN = element(
        name="R1304",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    IndustryCode4: X12AN = element(
        name="R1305",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    IndustryCode5: X12AN = element(
        name="R1306",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="R1307",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="R1308",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="R1309",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="R1310",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description2: Optional[X12AN] = element(
        name="R1311",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Quantity2: Optional[X12R] = element(
        name="R1312",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
