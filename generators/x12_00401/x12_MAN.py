# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MAN(Segment):
    """
    MAN - Marks and Numbers
    
    Description:
        To indicate identifying marks and numbers for shipping containers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MAN/
    """
    _id: Literal["MAN"] = id_element(name="MAN")

    Qualifier: X12ID = element(
        name="MAN01",
        description="Marks and Numbers Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Number: X12AN = element(
        name="MAN02",
        description="Marks and Numbers",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    MarksAndNumbers: Optional[X12AN] = element(
        name="MAN03",
        description="Marks and Numbers",
        min_length=1,
        max_length=48,
    )

    Qualifier2: Optional[X12ID] = element(
        name="MAN04",
        description="Marks and Numbers Qualifier",
        min_length=1,
        max_length=2,
    )

    Number2: Optional[X12AN] = element(
        name="MAN05",
        description="Marks and Numbers",
        min_length=1,
        max_length=48,
    )

    MarksAndNumbers2: Optional[X12AN] = element(
        name="MAN06",
        description="Marks and Numbers",
        min_length=1,
        max_length=48,
    )
