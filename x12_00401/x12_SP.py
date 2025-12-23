# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SP(Segment):
    """
    SP - Special Program
    
    Description:
        To provide the receiving educational institution or agency with information concerning the student's participation in special education programs or other programs and services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SP/
    """
    _id: Literal["SP"] = id_element(name="SP")

    SpecialProgramCategoryCode: Optional[X12ID] = element(
        name="SP01",
        description="Special Program Category Code",
        min_length=1,
        max_length=2,
    )

    Percent: Optional[X12R] = element(
        name="SP02",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    ProgramParticipationAndServicesCode: Optional[X12ID] = element(
        name="SP03",
        description="Program Participation and Services Code",
        min_length=1,
        max_length=2,
    )

    ProgramAndServicesFundingSourceCode: Optional[X12ID] = element(
        name="SP04",
        description="Program and Services Funding Source Code",
    )

    Name: Optional[X12AN] = element(
        name="SP05",
        description="Name",
        min_length=1,
        max_length=60,
    )
