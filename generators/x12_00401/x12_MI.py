# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class MI(Segment):
    """
    MI - Media Information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MI/
    """
    _id: Literal["MI"] = id_element(name="MI")

    MediaTypeIdentifier: X12ID = element(
        name="MI01",
        description="Media Type Identifier",
        mandatory=True,
    )

    Amount: Optional[X12Nn] = element(
        name="MI02",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount2: Optional[X12Nn] = element(
        name="MI03",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount3: Optional[X12Nn] = element(
        name="MI04",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="MI05",
        description="Description",
        min_length=1,
        max_length=80,
    )
