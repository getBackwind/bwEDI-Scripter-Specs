# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class C8(Segment):
    """
    C8 - Certifications and Clauses
    
    Description:
        To specify applicable certifications and clauses
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/C8/
    """
    _id: Literal["C8"] = id_element(name="C8")

    LadingLineItemNumber: Optional[X12Nn] = element(
        name="C801",
        description="Lading Line Item Number",
        min_length=1,
        max_length=3,
    )

    CertificationClauseCode: Optional[X12ID] = element(
        name="C802",
        description="Certification/Clause Code",
        min_length=2,
        max_length=2,
    )

    CertificationClauseText: Optional[X12AN] = element(
        name="C803",
        description="Certification/Clause Text",
        min_length=2,
        max_length=60,
    )

    ShipperSExportDeclarationRequirements: Optional[X12AN] = element(
        name="C804",
        description="Shipper's Export Declaration Requirements",
        min_length=1,
        max_length=2,
    )
