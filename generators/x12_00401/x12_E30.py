# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class E30(Segment):
    """
    E30 - Data Element Attributes
    
    Description:
        To provide the data element attributes for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/E30/
    """
    _id: Literal["E30"] = id_element(name="E30")

    MaintenanceOperationCode: X12ID = element(
        name="E3001",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DataElementReferenceNumber: X12Nn = element(
        name="E3002",
        description="Data Element Reference Number",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    DataElementType: X12ID = element(
        name="E3003",
        description="Data Element Type",
        mandatory=True,
    )

    MinimumLength: X12Nn = element(
        name="E3004",
        description="Minimum Length",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    MaximumLength: X12Nn = element(
        name="E3005",
        description="Maximum Length",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    Description: Optional[X12AN] = element(
        name="E3006",
        description="Description",
        min_length=1,
        max_length=80,
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="E3007",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )

    DataElementReferenceNumber2: Optional[X12Nn] = element(
        name="E3008",
        description="Data Element Reference Number",
        min_length=1,
        max_length=4,
    )

    CodeListReference: Optional[X12AN] = element(
        name="E3009",
        description="Code List Reference",
        min_length=1,
        max_length=6,
    )
