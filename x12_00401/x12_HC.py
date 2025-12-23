# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class HC(Segment):
    """
    HC - Health Condition
    
    Description:
        To provide the receiving district with notice of the student's health condition status
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/HC/
    """
    _id: Literal["HC"] = id_element(name="HC")

    DiseaseConditionTypeCode: X12ID = element(
        name="HC01",
        description="Disease Condition Type Code",
        mandatory=True,
        min_length=3,
        max_length=6,
    )

    MedicalTreatmentTypeCode: Optional[X12ID] = element(
        name="HC02",
        description="Medical Treatment Type Code",
        min_length=5,
        max_length=5,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="HC03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="HC04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="HC05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
