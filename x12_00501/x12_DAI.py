# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class DAI(Segment):
    """
    DAI - Appendix Information
    
    Description:
        To provide appendix information for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DAI/
    """
    _id: Literal["DAI"] = id_element(name="DAI")

    MaintenanceOperationCode: X12ID = element(
        name="DAI01",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CodeListReference: X12AN = element(
        name="DAI02",
        description="Code List Reference",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="DAI03",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )
