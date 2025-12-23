# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class INS(Segment):
    """
    INS - Insured Benefit
    
    Description:
        To provide benefit information on insured entities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/INS/
    """
    _id: Literal["INS"] = id_element(name="INS")

    YesNoConditionOrResponseCode: X12ID = element(
        name="INS01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    IndividualRelationshipCode: X12ID = element(
        name="INS02",
        description="Individual Relationship Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MaintenanceTypeCode: Optional[X12ID] = element(
        name="INS03",
        description="Maintenance Type Code",
        min_length=3,
        max_length=3,
    )

    MaintenanceReasonCode: Optional[X12ID] = element(
        name="INS04",
        description="Maintenance Reason Code",
        min_length=2,
        max_length=2,
    )

    BenefitStatusCode: Optional[X12ID] = element(
        name="INS05",
        description="Benefit Status Code",
        min_length=1,
        max_length=1,
    )

    ConsolidatedOmnibusBudgetReconciliationActCOBRAQualifyingEventCode: Optional[X12ID] = element(
        name="INS07",
        description="Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying Event Code",
        min_length=1,
        max_length=2,
    )

    EmploymentStatusCode: Optional[X12ID] = element(
        name="INS08",
        description="Employment Status Code",
        min_length=2,
        max_length=2,
    )

    StudentStatusCode: Optional[X12ID] = element(
        name="INS09",
        description="Student Status Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="INS10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="INS11",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="INS12",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    ConfidentialityCode: Optional[X12ID] = element(
        name="INS13",
        description="Confidentiality Code",
        min_length=1,
        max_length=1,
    )

    CityName: Optional[X12AN] = element(
        name="INS14",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="INS15",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="INS16",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    Number: Optional[X12Nn] = element(
        name="INS17",
        description="Number",
        min_length=1,
        max_length=9,
    )
