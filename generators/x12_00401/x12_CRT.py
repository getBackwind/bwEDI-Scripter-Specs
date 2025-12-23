# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CRT(Segment):
    """
    CRT - Contractor Report Type
    
    Description:
        To identify the contractor report type, type of units reported, status information, and related reporting details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CRT/
    """
    _id: Literal["CRT"] = id_element(name="CRT")

    ReportTypeCode: X12ID = element(
        name="CRT01",
        description="Report Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    BreakdownStructureDetailCode: Optional[X12ID] = element(
        name="CRT04",
        description="Breakdown Structure Detail Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="CRT05",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    RateOrValueTypeCode: Optional[X12ID] = element(
        name="CRT06",
        description="Rate or Value Type Code",
        min_length=1,
        max_length=2,
    )

    ContractActionCode: Optional[X12ID] = element(
        name="CRT07",
        description="Contract Action Code",
        min_length=2,
        max_length=2,
    )

    ProgramTypeCode: Optional[X12ID] = element(
        name="CRT08",
        description="Program Type Code",
        min_length=2,
        max_length=2,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="CRT09",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="CRT10",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )
