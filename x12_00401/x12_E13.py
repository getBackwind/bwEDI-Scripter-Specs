# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class E13(Segment):
    """
    E13 - Segment Order in Transaction Set
    
    Description:
        To provide the list of segments in a transaction set for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/E13/
    """
    _id: Literal["E13"] = id_element(name="E13")

    MaintenanceOperationCode: X12ID = element(
        name="E1301",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PositionInSet: X12Nn = element(
        name="E1302",
        description="Position in Set",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    SectionDesignator: Optional[X12ID] = element(
        name="E1303",
        description="Section Designator",
    )

    SegmentIDCode: Optional[X12ID] = element(
        name="E1304",
        description="Segment ID Code",
        min_length=2,
        max_length=3,
    )

    RequirementDesignator: Optional[X12ID] = element(
        name="E1305",
        description="Requirement Designator",
    )

    MaximumUse: Optional[X12Nn] = element(
        name="E1306",
        description="Maximum Use",
        min_length=1,
        max_length=7,
    )

    LoopName: Optional[X12AN] = element(
        name="E1307",
        description="Loop Name",
        min_length=2,
        max_length=4,
    )

    LoopRepeatCount: Optional[X12Nn] = element(
        name="E1308",
        description="Loop Repeat Count",
        min_length=1,
        max_length=7,
    )

    LoopLevelNumber: Optional[X12Nn] = element(
        name="E1309",
        description="Loop Level Number",
        min_length=1,
        max_length=1,
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="E1310",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )
