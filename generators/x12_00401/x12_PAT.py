# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PAT(Segment):
    """
    PAT - Patient Information
    
    Description:
        To supply patient information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PAT/
    """
    _id: Literal["PAT"] = id_element(name="PAT")

    IndividualRelationshipCode: Optional[X12ID] = element(
        name="PAT01",
        description="Individual Relationship Code",
        min_length=2,
        max_length=2,
    )

    PatientLocationCode: Optional[X12ID] = element(
        name="PAT02",
        description="Patient Location Code",
        min_length=1,
        max_length=1,
    )

    EmploymentStatusCode: Optional[X12ID] = element(
        name="PAT03",
        description="Employment Status Code",
        min_length=2,
        max_length=2,
    )

    StudentStatusCode: Optional[X12ID] = element(
        name="PAT04",
        description="Student Status Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="PAT05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="PAT06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="PAT07",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="PAT08",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PAT09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
