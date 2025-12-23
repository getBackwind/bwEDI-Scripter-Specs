# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PRT(Segment):
    """
    PRT - Part Disposition
    
    Description:
        To specify the disposition of the removed part, subassembly or assembly
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PRT/
    """
    _id: Literal["PRT"] = id_element(name="PRT")

    DispositionCode: X12AN = element(
        name="PRT01",
        description="Disposition Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="PRT02",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="PRT03",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PRT04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
