# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BCI(Segment):
    """
    BCI - Basic Claim Information
    
    Description:
        To identify information basic to the processing of any claims transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BCI/
    """
    _id: Literal["BCI"] = id_element(name="BCI")

    IndustryCode: Optional[X12AN] = element(
        name="BCI01",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    InsuranceTypeCode: Optional[X12ID] = element(
        name="BCI02",
        description="Insurance Type Code",
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BCI03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="BCI04",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="BCI05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="BCI06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    ReportTypeCode: Optional[X12ID] = element(
        name="BCI07",
        description="Report Type Code",
        min_length=2,
        max_length=2,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="BCI08",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
