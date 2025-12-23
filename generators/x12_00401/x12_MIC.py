# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class MIC(Segment):
    """
    MIC - Mortgage Insurance Coverage
    
    Description:
        To describe the type and extent of mortgage insurance
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MIC/
    """
    _id: Literal["MIC"] = id_element(name="MIC")

    MortgageInsuranceApplicationType: X12ID = element(
        name="MIC01",
        description="Mortgage Insurance Application Type",
        mandatory=True,
    )

    MortgageInsuranceCoverageTypeCode: Optional[X12ID] = element(
        name="MIC02",
        description="Mortgage Insurance Coverage Type Code",
        min_length=1,
        max_length=1,
    )

    MortgageInsuranceCertificateTypeCode: Optional[X12ID] = element(
        name="MIC03",
        description="Mortgage Insurance Certificate Type Code",
        min_length=1,
        max_length=1,
    )

    Percent: Optional[X12R] = element(
        name="MIC04",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    PremiumRatePatternCode: Optional[X12ID] = element(
        name="MIC05",
        description="Premium Rate Pattern Code",
        min_length=1,
        max_length=1,
    )

    MortgageInsuranceDurationCode: Optional[X12ID] = element(
        name="MIC06",
        description="Mortgage Insurance Duration Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="MIC08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MortgageInsuranceRenewalOptionCode: Optional[X12ID] = element(
        name="MIC09",
        description="Mortgage Insurance Renewal Option Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="MIC10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    TermsTypeCode: Optional[X12ID] = element(
        name="MIC11",
        description="Terms Type Code",
        min_length=2,
        max_length=2,
    )

    MortgageInsurancePremiumTypeCode: Optional[X12ID] = element(
        name="MIC12",
        description="Mortgage Insurance Premium Type Code",
        min_length=1,
        max_length=1,
    )

    Amount: Optional[X12Nn] = element(
        name="MIC13",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    PremiumSourceEntityCode: Optional[X12ID] = element(
        name="MIC14",
        description="Premium Source Entity Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="MIC15",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="MIC16",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="MIC17",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
