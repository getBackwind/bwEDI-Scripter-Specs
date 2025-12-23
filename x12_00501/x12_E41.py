# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class E41(Segment):
    """
    E41 - Composite Header Information
    
    Description:
        To provide for grouping the data elements by composite ID value for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E41/
    """
    _id: Literal["E41"] = id_element(name="E41")

    MaintenanceOperationCode: X12ID = element(
        name="E4101",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DataElementReferenceNumber: X12Nn = element(
        name="E4102",
        description="Data Element Reference Number",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    Description: Optional[X12AN] = element(
        name="E4103",
        description="Description",
        min_length=1,
        max_length=80,
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="E4104",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )
