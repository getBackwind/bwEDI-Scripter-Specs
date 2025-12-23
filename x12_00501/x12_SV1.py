# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SV1(Segment):
    """
    SV1 - Professional Service
    
    Description:
        To specify the service line item detail for a health care professional
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SV1/
    """
    _id: Literal["SV1"] = id_element(name="SV1")

    MonetaryAmount: Optional[X12R] = element(
        name="SV102",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="SV103",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="SV104",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    FacilityCodeValue: Optional[X12AN] = element(
        name="SV105",
        description="Facility Code Value",
        min_length=1,
        max_length=2,
    )

    ServiceTypeCode: Optional[X12ID] = element(
        name="SV106",
        description="Service Type Code",
        min_length=1,
        max_length=2,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="SV108",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SV109",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    MultipleProcedureCode: Optional[X12ID] = element(
        name="SV110",
        description="Multiple Procedure Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SV111",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="SV112",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReviewCode: Optional[X12ID] = element(
        name="SV113",
        description="Review Code",
        min_length=1,
        max_length=1,
    )

    NationalOrLocalAssignedReviewValue: Optional[X12AN] = element(
        name="SV114",
        description="National or Local Assigned Review Value",
        min_length=1,
        max_length=2,
    )

    CopayStatusCode: Optional[X12ID] = element(
        name="SV115",
        description="Copay Status Code",
        min_length=1,
        max_length=1,
    )

    HealthCareProfessionalShortageAreaCode: Optional[X12ID] = element(
        name="SV116",
        description="Health Care Professional Shortage Area Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="SV117",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    PostalCode: Optional[X12ID] = element(
        name="SV118",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="SV119",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    LevelOfCareCode: Optional[X12ID] = element(
        name="SV120",
        description="Level of Care Code",
        min_length=1,
        max_length=1,
    )

    ProviderAgreementCode: Optional[X12ID] = element(
        name="SV121",
        description="Provider Agreement Code",
        min_length=1,
        max_length=1,
    )
