# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SUP(Segment):
    """
    SUP - Supplementary Information
    
    Description:
        To provide processible supplementary information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SUP/
    """
    _id: Literal["SUP"] = id_element(name="SUP")

    SupplementaryInformationQualifier: X12ID = element(
        name="SUP01",
        description="Supplementary Information Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    CertificationClauseCode: Optional[X12ID] = element(
        name="SUP02",
        description="Certification/Clause Code",
        min_length=2,
        max_length=2,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="SUP03",
        description="Free-form Message",
        min_length=1,
        max_length=60,
    )

    PrintOptionCode: Optional[X12ID] = element(
        name="SUP04",
        description="Print Option Code",
        min_length=2,
        max_length=2,
    )
