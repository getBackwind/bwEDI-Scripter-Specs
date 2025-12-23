# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CLI(Segment):
    """
    CLI - Cost Line Item
    
    Description:
        To identify the cost line items associated with a specific reporting structure reference (i.e., a work breakdown structure) or summary project level reference
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CLI/
    """
    _id: Literal["CLI"] = id_element(name="CLI")

    EntityIdentifierCode: Optional[X12ID] = element(
        name="CLI01",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    BreakdownStructureDetailCode: Optional[X12ID] = element(
        name="CLI02",
        description="Breakdown Structure Detail Code",
        min_length=2,
        max_length=2,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="CLI03",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="CLI04",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    RateOrValueTypeCode: Optional[X12ID] = element(
        name="CLI05",
        description="Rate or Value Type Code",
        min_length=1,
        max_length=2,
    )

    ContractTypeCode: Optional[X12ID] = element(
        name="CLI06",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )
