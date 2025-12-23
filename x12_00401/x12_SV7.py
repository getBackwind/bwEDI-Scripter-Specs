# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SV7(Segment):
    """
    SV7 - Drug Adjudication
    
    Description:
        To specify the claim service detail for drug services that have been adjudicated
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SV7/
    """
    _id: Literal["SV7"] = id_element(name="SV7")

    ReferenceIdentification: Optional[X12AN] = element(
        name="SV701",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="SV702",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    PrescriptionDenialOverrideCode: Optional[X12ID] = element(
        name="SV703",
        description="Prescription Denial Override Code",
        min_length=2,
        max_length=2,
    )

    CoverageLevelCode: X12ID = element(
        name="SV704",
        description="Coverage Level Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    ProductProcessCharacteristicCode: X12ID = element(
        name="SV705",
        description="Product/Process Characteristic Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SV706",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
