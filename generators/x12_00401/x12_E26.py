# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class E26(Segment):
    """
    E26 - Element Sequence in Composite
    
    Description:
        To provide the detail information related to the sequence of the subelements in a composite data element (segment) for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/E26/
    """
    _id: Literal["E26"] = id_element(name="E26")

    MaintenanceOperationCode: X12ID = element(
        name="E2601",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PositionInComposite: X12Nn = element(
        name="E2602",
        description="Position in Composite",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    DataElementReferenceNumber: X12Nn = element(
        name="E2603",
        description="Data Element Reference Number",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    RequirementDesignator: X12ID = element(
        name="E2604",
        description="Requirement Designator",
        mandatory=True,
    )

    DataElementType: Optional[X12ID] = element(
        name="E2605",
        description="Data Element Type",
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="E2606",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )
