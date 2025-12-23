# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class E20(Segment):
    """
    E20 - Segment Header Information
    
    Description:
        To provide for grouping the data elements by segment ID value for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/E20/
    """
    _id: Literal["E20"] = id_element(name="E20")

    MaintenanceOperationCode: X12ID = element(
        name="E2001",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    SegmentIDCode: X12ID = element(
        name="E2002",
        description="Segment ID Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    Description: Optional[X12AN] = element(
        name="E2003",
        description="Description",
        min_length=1,
        max_length=80,
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="E2004",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )
