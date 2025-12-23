# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SV4(Segment):
    """
    SV4 - Drug Service
    
    Description:
        To specify the claim service detail for prescription drugs
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SV4/
    """
    _id: Literal["SV4"] = id_element(name="SV4")

    ReferenceIdentification: X12AN = element(
        name="SV401",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="SV403",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SV404",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    DispenseAsWrittenCode: Optional[X12ID] = element(
        name="SV405",
        description="Dispense as Written Code",
        min_length=1,
        max_length=1,
    )

    LevelOfServiceCode: Optional[X12ID] = element(
        name="SV406",
        description="Level of Service Code",
        min_length=1,
        max_length=3,
    )

    PrescriptionOriginCode: Optional[X12ID] = element(
        name="SV407",
        description="Prescription Origin Code",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="SV408",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SV409",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="SV410",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    UnitDoseCode: Optional[X12ID] = element(
        name="SV411",
        description="Unit Dose Code",
        min_length=1,
        max_length=1,
    )

    BasisOfCostDeterminationCode: Optional[X12ID] = element(
        name="SV412",
        description="Basis of Cost Determination Code",
        min_length=1,
        max_length=1,
    )

    BasisOfDaysSupplyDeterminationCode: Optional[X12ID] = element(
        name="SV413",
        description="Basis of Days Supply Determination Code",
        min_length=1,
        max_length=1,
    )

    DosageFormCode: Optional[X12ID] = element(
        name="SV414",
        description="Dosage Form Code",
        min_length=2,
        max_length=2,
    )

    CopayStatusCode: Optional[X12ID] = element(
        name="SV415",
        description="Copay Status Code",
        min_length=1,
        max_length=1,
    )

    PatientLocationCode: Optional[X12ID] = element(
        name="SV416",
        description="Patient Location Code",
        min_length=1,
        max_length=1,
    )

    LevelOfCareCode: Optional[X12ID] = element(
        name="SV417",
        description="Level of Care Code",
        min_length=1,
        max_length=1,
    )

    PriorAuthorizationTypeCode: Optional[X12ID] = element(
        name="SV418",
        description="Prior Authorization Type Code",
        min_length=1,
        max_length=1,
    )
