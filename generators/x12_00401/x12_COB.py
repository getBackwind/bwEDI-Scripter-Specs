# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class COB(Segment):
    """
    COB - Coordination of Benefits
    
    Description:
        To supply information on coordination of benefits
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/COB/
    """
    _id: Literal["COB"] = id_element(name="COB")

    PayerResponsibilitySequenceNumberCode: Optional[X12ID] = element(
        name="COB01",
        description="Payer Responsibility Sequence Number Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="COB02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    CoordinationOfBenefitsCode: Optional[X12ID] = element(
        name="COB03",
        description="Coordination of Benefits Code",
        min_length=1,
        max_length=1,
    )
