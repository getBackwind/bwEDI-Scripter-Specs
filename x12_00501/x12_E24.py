# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class E24(Segment):
    """
    E24 - Data Element Sequence in a Segment or Composite
    
    Description:
        To provide the detail information related to the sequence of the data elements in a segment or composite for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E24/
    """
    _id: Literal["E24"] = id_element(name="E24")

    MaintenanceOperationCode: X12ID = element(
        name="E2401",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PositionInSegmentOrComposite: X12Nn = element(
        name="E2402",
        description="Position in Segment or Composite",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    DataElementReferenceNumber: X12Nn = element(
        name="E2403",
        description="Data Element Reference Number",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    RequirementDesignator: X12ID = element(
        name="E2404",
        description="Requirement Designator",
        mandatory=True,
    )

    DataElementUsageType: Optional[X12ID] = element(
        name="E2405",
        description="Data Element Usage Type",
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="E2406",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )

    Count: Optional[X12Nn] = element(
        name="E2407",
        description="Count",
        min_length=1,
        max_length=9,
    )
