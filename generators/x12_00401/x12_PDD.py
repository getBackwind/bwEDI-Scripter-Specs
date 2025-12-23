# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PDD(Segment):
    """
    PDD - Pricing Data Detail
    
    Description:
        To provide the rates, direct input, and pricing factors for each element of work, cross-referenced to an applicable request or submission
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PDD/
    """
    _id: Literal["PDD"] = id_element(name="PDD")

    AssignedIdentification: X12AN = element(
        name="PDD01",
        description="Assigned Identification",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    Quantity: Optional[X12R] = element(
        name="PDD02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PDD03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12R] = element(
        name="PDD04",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    ProposalDataDetailIdentifierCode: Optional[X12ID] = element(
        name="PDD05",
        description="Proposal Data Detail Identifier Code",
        min_length=2,
        max_length=2,
    )
