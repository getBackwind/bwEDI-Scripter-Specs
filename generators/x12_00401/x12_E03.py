# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class E03(Segment):
    """
    E03 - Interchange Order of Segments
    
    Description:
        To provide information related to the interchange order table of the control segments for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/E03/
    """
    _id: Literal["E03"] = id_element(name="E03")

    MaintenanceOperationCode: X12ID = element(
        name="E0301",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    LevelNumber: X12ID = element(
        name="E0302",
        description="Level Number",
        mandatory=True,
    )

    SegmentIDCode: X12ID = element(
        name="E0303",
        description="Segment ID Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    EnvelopeIndicator: X12ID = element(
        name="E0304",
        description="Envelope Indicator",
        mandatory=True,
    )

    RequirementDesignator: X12ID = element(
        name="E0305",
        description="Requirement Designator",
        mandatory=True,
    )

    MaximumUse: X12Nn = element(
        name="E0306",
        description="Maximum Use",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="E0307",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )
