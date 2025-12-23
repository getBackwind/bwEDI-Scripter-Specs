# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class IGI(Segment):
    """
    IGI - Insurer or Guarantor Information
    
    Description:
        To identify the mortgage insurer or guarantor and provide information about the insurance coverage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IGI/
    """
    _id: Literal["IGI"] = id_element(name="IGI")

    InsurerGuarantorTypeCode: X12ID = element(
        name="IGI01",
        description="Insurer Guarantor Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="IGI02",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="IGI03",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    MortgageInsuranceCoverageTypeCode: Optional[X12ID] = element(
        name="IGI04",
        description="Mortgage Insurance Coverage Type Code",
        min_length=1,
        max_length=1,
    )

    InsurerCoverageIndicatorCode: Optional[X12ID] = element(
        name="IGI05",
        description="Insurer Coverage Indicator Code",
        min_length=1,
        max_length=1,
    )

    PayerResponsibilitySequenceNumberCode: Optional[X12ID] = element(
        name="IGI06",
        description="Payer Responsibility Sequence Number Code",
        min_length=1,
        max_length=1,
    )
