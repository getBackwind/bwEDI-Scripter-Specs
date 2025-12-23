# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12R


class THE(Segment):
    """
    THE - Screen Theater Identification
    
    Description:
        To identify the theater and screen for accompanying detail
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/THE/
    """
    _id: Literal["THE"] = id_element(name="THE")

    IdentificationCode: X12AN = element(
        name="THE01",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    Name: X12AN = element(
        name="THE02",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="THE03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Quantity: Optional[X12R] = element(
        name="THE04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="THE05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
