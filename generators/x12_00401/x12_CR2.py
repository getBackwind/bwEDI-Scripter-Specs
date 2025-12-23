# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class CR2(Segment):
    """
    CR2 - Chiropractic Certification
    
    Description:
        To supply information related to the chiropractic service rendered to a patient
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CR2/
    """
    _id: Literal["CR2"] = id_element(name="CR2")

    Count: Optional[X12Nn] = element(
        name="CR201",
        description="Count",
        min_length=1,
        max_length=9,
    )

    Quantity: Optional[X12R] = element(
        name="CR202",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    SubluxationLevelCode: Optional[X12ID] = element(
        name="CR203",
        description="Subluxation Level Code",
        min_length=2,
        max_length=3,
    )

    SubluxationLevelCode2: Optional[X12ID] = element(
        name="CR204",
        description="Subluxation Level Code",
        min_length=2,
        max_length=3,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="CR205",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity2: Optional[X12R] = element(
        name="CR206",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="CR207",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    NatureOfConditionCode: Optional[X12ID] = element(
        name="CR208",
        description="Nature of Condition Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CR209",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="CR210",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description2: Optional[X12AN] = element(
        name="CR211",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="CR212",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
