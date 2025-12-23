# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class CR8(Segment):
    """
    CR8 - Pacemaker Certification
    
    Description:
        To supply information related to Pacemaker registry
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CR8/
    """
    _id: Literal["CR8"] = id_element(name="CR8")

    ImplantTypeCode: X12ID = element(
        name="CR801",
        description="Implant Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ImplantStatusCode: X12ID = element(
        name="CR802",
        description="Implant Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="CR803",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: X12DT = element(
        name="CR804",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification: X12AN = element(
        name="CR805",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: X12AN = element(
        name="CR806",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification3: X12AN = element(
        name="CR807",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="CR808",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: X12ID = element(
        name="CR809",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
