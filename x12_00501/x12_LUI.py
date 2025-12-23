# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LUI(Segment):
    """
    LUI - Language Use
    
    Description:
        To specify language, type of usage, and proficiency or fluency
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LUI/
    """
    _id: Literal["LUI"] = id_element(name="LUI")

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="LUI01",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="LUI02",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Description: Optional[X12AN] = element(
        name="LUI03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    UseOfLanguageIndicator: Optional[X12ID] = element(
        name="LUI04",
        description="Use of Language Indicator",
    )

    LanguageProficiencyIndicator: Optional[X12ID] = element(
        name="LUI05",
        description="Language Proficiency Indicator",
    )
