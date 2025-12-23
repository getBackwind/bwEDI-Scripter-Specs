# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TID(Segment):
    """
    TID - Task Identification
    
    Description:
        To identify the work task and activity, what type of task it is, and related information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TID/
    """
    _id: Literal["TID"] = id_element(name="TID")

    TaskIDQualifier: X12ID = element(
        name="TID01",
        description="Task ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TaskIdentifier: Optional[X12AN] = element(
        name="TID02",
        description="Task Identifier",
        min_length=1,
        max_length=20,
    )

    RelationshipTaskIdentifier: Optional[X12AN] = element(
        name="TID03",
        description="Relationship Task Identifier",
        min_length=1,
        max_length=20,
    )

    Description: Optional[X12AN] = element(
        name="TID04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    WorkStatusCode: Optional[X12ID] = element(
        name="TID05",
        description="Work Status Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="TID06",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="TID07",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="TID08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Level: Optional[X12AN] = element(
        name="TID09",
        description="Level",
        min_length=1,
        max_length=3,
    )
