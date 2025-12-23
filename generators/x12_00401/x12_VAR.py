# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class VAR(Segment):
    """
    VAR - Credit File Variation
    
    Description:
        To identify variations discovered in credit items or tradelines
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/VAR/
    """
    _id: Literal["VAR"] = id_element(name="VAR")

    IdentificationCode: X12AN = element(
        name="VAR01",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="VAR02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    CreditFileVariationCode: Optional[X12ID] = element(
        name="VAR03",
        description="Credit File Variation Code",
        min_length=2,
        max_length=2,
    )

    CreditFileVariationCode2: Optional[X12ID] = element(
        name="VAR04",
        description="Credit File Variation Code",
        min_length=2,
        max_length=2,
    )

    CreditFileVariationCode3: Optional[X12ID] = element(
        name="VAR05",
        description="Credit File Variation Code",
        min_length=2,
        max_length=2,
    )

    CreditFileVariationCode4: Optional[X12ID] = element(
        name="VAR06",
        description="Credit File Variation Code",
        min_length=2,
        max_length=2,
    )

    CreditFileVariationCode5: Optional[X12ID] = element(
        name="VAR07",
        description="Credit File Variation Code",
        min_length=2,
        max_length=2,
    )
