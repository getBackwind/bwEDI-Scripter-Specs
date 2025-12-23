# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class CR6(Segment):
    """
    CR6 - Home Health Care Certification
    
    Description:
        To supply information related to the certification of a home health care patient
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CR6/
    """
    _id: Literal["CR6"] = id_element(name="CR6")

    PrognosisCode: X12ID = element(
        name="CR601",
        description="Prognosis Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="CR602",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="CR603",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="CR604",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Date2: Optional[X12DT] = element(
        name="CR605",
        description="Date",
        min_length=8,
        max_length=8,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CR606",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: X12ID = element(
        name="CR607",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CertificationTypeCode: X12ID = element(
        name="CR608",
        description="Certification Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date3: Optional[X12DT] = element(
        name="CR609",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="CR610",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    MedicalCodeValue: Optional[X12AN] = element(
        name="CR611",
        description="Medical Code Value",
        min_length=1,
        max_length=15,
    )

    Date4: Optional[X12DT] = element(
        name="CR612",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date5: Optional[X12DT] = element(
        name="CR613",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date6: Optional[X12DT] = element(
        name="CR614",
        description="Date",
        min_length=8,
        max_length=8,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="CR615",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="CR616",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    PatientLocationCode: Optional[X12ID] = element(
        name="CR617",
        description="Patient Location Code",
        min_length=1,
        max_length=1,
    )

    Date7: Optional[X12DT] = element(
        name="CR618",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date8: Optional[X12DT] = element(
        name="CR619",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date9: Optional[X12DT] = element(
        name="CR620",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date10: Optional[X12DT] = element(
        name="CR621",
        description="Date",
        min_length=8,
        max_length=8,
    )
