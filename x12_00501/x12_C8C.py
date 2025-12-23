# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class C8C(Segment):
    """
    C8C - Certifications Clauses Continuation
    
    Description:
        To specify additional applicable certifications and clauses
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/C8C/
    """
    _id: Literal["C8C"] = id_element(name="C8C")

    CertificationClauseText: X12AN = element(
        name="C8C01",
        description="Certification/Clause Text",
        mandatory=True,
        min_length=2,
        max_length=60,
    )

    CertificationClauseText2: Optional[X12AN] = element(
        name="C8C02",
        description="Certification/Clause Text",
        min_length=2,
        max_length=60,
    )

    CertificationClauseText3: Optional[X12AN] = element(
        name="C8C03",
        description="Certification/Clause Text",
        min_length=2,
        max_length=60,
    )
