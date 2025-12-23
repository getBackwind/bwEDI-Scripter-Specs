# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class RDT(Segment):
    """
    RDT - Revision Date/Time
    
    Description:
        To specify the revision level of the electronic data item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RDT/
    """
    _id: Literal["RDT"] = id_element(name="RDT")

    RevisionLevelCode: Optional[X12ID] = element(
        name="RDT01",
        description="Revision Level Code",
        min_length=1,
        max_length=1,
    )

    RevisionValue: Optional[X12AN] = element(
        name="RDT02",
        description="Revision Value",
        min_length=1,
        max_length=30,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="RDT03",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="RDT04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="RDT05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="RDT06",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
