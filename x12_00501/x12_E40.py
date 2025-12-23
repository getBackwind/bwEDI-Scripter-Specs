# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class E40(Segment):
    """
    E40 - EDI Standards Note Reference
    
    Description:
        To transmit information relative to comments and notes within the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E40/
    """
    _id: Literal["E40"] = id_element(name="E40")

    MaintenanceOperationCode: X12ID = element(
        name="E4001",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    NoteIdentificationNumber: X12Nn = element(
        name="E4002",
        description="Note Identification Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    ElectronicFormNoteReferenceCode: X12ID = element(
        name="E4003",
        description="Electronic Form Note Reference Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="E4004",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )
