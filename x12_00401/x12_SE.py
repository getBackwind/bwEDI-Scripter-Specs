# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class SE(Segment):
    """
    SE - Transaction Set Trailer
    
    Description:
        To indicate the end of the transaction set and provide the count of the transmitted segments (including the beginning (ST) and ending (SE) segments)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SE/
    """
    _id: Literal["SE"] = id_element(name="SE")

    SegmentsCount: X12AN = element(
        name="SE01",
        description="Number of Included Segments",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    TransactionSetID: X12AN = element(
        name="SE02",
        description="Transaction Set Control Number",
        mandatory=True,
        min_length=4,
        max_length=9,
    )
