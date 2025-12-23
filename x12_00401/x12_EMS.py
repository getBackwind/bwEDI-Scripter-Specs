# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class EMS(Segment):
    """
    EMS - Employment Position
    
    Description:
        To describe employment position
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/EMS/
    """
    _id: Literal["EMS"] = id_element(name="EMS")

    Description: Optional[X12AN] = element(
        name="EMS01",
        description="Description",
        min_length=1,
        max_length=80,
    )

    EmploymentClassCode: Optional[X12ID] = element(
        name="EMS02",
        description="Employment Class Code",
        min_length=2,
        max_length=2,
    )

    OccupationCode: Optional[X12ID] = element(
        name="EMS03",
        description="Occupation Code",
        min_length=4,
        max_length=6,
    )

    EmploymentStatusCode: Optional[X12ID] = element(
        name="EMS04",
        description="Employment Status Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="EMS05",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="EMS06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="EMS07",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
