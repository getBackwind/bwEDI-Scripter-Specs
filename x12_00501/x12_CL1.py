# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class CL1(Segment):
    """
    CL1 - Claim Codes
    
    Description:
        To supply information specific to hospital claims
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CL1/
    """
    _id: Literal["CL1"] = id_element(name="CL1")

    AdmissionTypeCode: Optional[X12ID] = element(
        name="CL101",
        description="Admission Type Code",
        min_length=1,
        max_length=1,
    )

    AdmissionSourceCode: Optional[X12ID] = element(
        name="CL102",
        description="Admission Source Code",
        min_length=1,
        max_length=1,
    )

    PatientStatusCode: Optional[X12ID] = element(
        name="CL103",
        description="Patient Status Code",
        min_length=1,
        max_length=2,
    )

    NursingHomeResidentialStatusCode: Optional[X12ID] = element(
        name="CL104",
        description="Nursing Home Residential Status Code",
        min_length=1,
        max_length=1,
    )
