# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class TBI(Segment):
    """
    TBI - Trade Line Bureau Identifier
    
    Description:
        To identify the credit repository and the associated credit files or hit levels for a particular item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TBI/
    """
    _id: Literal["TBI"] = id_element(name="TBI")

    IdentificationCode: Optional[X12AN] = element(
        name="TBI01",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="TBI02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="TBI03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="TBI04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification4: Optional[X12AN] = element(
        name="TBI05",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification5: Optional[X12AN] = element(
        name="TBI06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification6: Optional[X12AN] = element(
        name="TBI07",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification7: Optional[X12AN] = element(
        name="TBI08",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
