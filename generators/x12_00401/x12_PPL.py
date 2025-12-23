# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class PPL(Segment):
    """
    PPL - Price Support Data
    
    Description:
        To provide information about pricing support
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PPL/
    """
    _id: Literal["PPL"] = id_element(name="PPL")

    AcquisitionDataCode: Optional[X12ID] = element(
        name="PPL01",
        description="Acquisition Data Code",
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="PPL02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="PPL03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Description: Optional[X12AN] = element(
        name="PPL04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ProposalDataDetailIdentifierCode: Optional[X12ID] = element(
        name="PPL05",
        description="Proposal Data Detail Identifier Code",
        min_length=2,
        max_length=2,
    )
