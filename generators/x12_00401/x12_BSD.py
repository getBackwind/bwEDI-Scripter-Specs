# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BSD(Segment):
    """
    BSD - Breakdown Structure Description
    
    Description:
        To define discrete line items within industry or government reports
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BSD/
    """
    _id: Literal["BSD"] = id_element(name="BSD")

    ReferenceIdentificationQualifier: X12ID = element(
        name="BSD01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BSD02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="BSD03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Level: Optional[X12AN] = element(
        name="BSD04",
        description="Level",
        min_length=1,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BSD05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    BreakdownStructureDetailCode: Optional[X12ID] = element(
        name="BSD06",
        description="Breakdown Structure Detail Code",
        min_length=2,
        max_length=2,
    )

    Level2: Optional[X12AN] = element(
        name="BSD07",
        description="Level",
        min_length=1,
        max_length=3,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BSD08",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )
