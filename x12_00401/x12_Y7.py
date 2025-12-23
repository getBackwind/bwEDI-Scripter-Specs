# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12Nn


class Y7(Segment):
    """
    Y7 - Priority
    
    Description:
        To assign a priority to a booking which would increase the possibility that this cargo would be booked on said voyage and not be shut out
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/Y7/
    """
    _id: Literal["Y7"] = id_element(name="Y7")

    Priority: Optional[X12Nn] = element(
        name="Y701",
        description="Priority",
        min_length=1,
        max_length=1,
    )

    PriorityCode: Optional[X12Nn] = element(
        name="Y702",
        description="Priority Code",
        min_length=1,
        max_length=1,
    )

    PriorityCodeQualifier: Optional[X12AN] = element(
        name="Y703",
        description="Priority Code Qualifier",
        min_length=1,
        max_length=1,
    )

    PortCallFileNumber: Optional[X12Nn] = element(
        name="Y704",
        description="Port Call File Number",
        min_length=4,
        max_length=4,
    )

    Date: Optional[X12DT] = element(
        name="Y705",
        description="Date",
        min_length=8,
        max_length=8,
    )
