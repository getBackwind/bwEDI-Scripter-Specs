# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class BEP(Segment):
    """
    BEP - Borrower Education Program
    
    Description:
        To identify the type and location of borrower education provided
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BEP/
    """
    _id: Literal["BEP"] = id_element(name="BEP")

    ProgramParticipationAndServicesCode: X12ID = element(
        name="BEP01",
        description="Program Participation and Services Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    InstructionalSettingCode: Optional[X12ID] = element(
        name="BEP02",
        description="Instructional Setting Code",
        min_length=1,
        max_length=2,
    )
