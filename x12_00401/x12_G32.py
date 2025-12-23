# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn, X12R


class G32(Segment):
    """
    G32 - Survey Question Response
    
    Description:
        To provide information in response to ad hoc survey questions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G32/
    """
    _id: Literal["G32"] = id_element(name="G32")

    Number: X12Nn = element(
        name="G3201",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="G3202",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="G3203",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Date: Optional[X12DT] = element(
        name="G3204",
        description="Date",
        min_length=8,
        max_length=8,
    )
