# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CLP(Segment):
    """
    CLP - Claim Level Data
    
    Description:
        To supply information common to all services of a claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CLP/
    """
    _id: Literal["CLP"] = id_element(name="CLP")

    ClaimSubmitterSIdentifier: X12AN = element(
        name="CLP01",
        description="Claim Submitter's Identifier",
        mandatory=True,
        min_length=1,
        max_length=38,
    )

    ClaimStatusCode: X12ID = element(
        name="CLP02",
        description="Claim Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    MonetaryAmount: X12R = element(
        name="CLP03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: X12R = element(
        name="CLP04",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="CLP05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ClaimFilingIndicatorCode: Optional[X12ID] = element(
        name="CLP06",
        description="Claim Filing Indicator Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CLP07",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    FacilityCodeValue: Optional[X12AN] = element(
        name="CLP08",
        description="Facility Code Value",
        min_length=1,
        max_length=2,
    )

    ClaimFrequencyTypeCode: Optional[X12ID] = element(
        name="CLP09",
        description="Claim Frequency Type Code",
        min_length=1,
        max_length=1,
    )

    PatientStatusCode: Optional[X12ID] = element(
        name="CLP10",
        description="Patient Status Code",
        min_length=1,
        max_length=2,
    )

    DiagnosisRelatedGroupDRGCode: Optional[X12ID] = element(
        name="CLP11",
        description="Diagnosis Related Group (DRG) Code",
        min_length=1,
        max_length=4,
    )

    Quantity: Optional[X12R] = element(
        name="CLP12",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="CLP13",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CLP14",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
