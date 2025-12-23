# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PTS(Segment):
    """
    PTS - Property Tax Status
    
    Description:
        To provide data required for proper notification or determination of applicable taxes applying to the transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PTS/
    """
    _id: Literal["PTS"] = id_element(name="PTS")

    StatusCode: X12ID = element(
        name="PTS01",
        description="Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="PTS02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    TaxServicePaymentCode: Optional[X12ID] = element(
        name="PTS03",
        description="Tax Service Payment Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="PTS04",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="PTS05",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    StatusCode2: Optional[X12ID] = element(
        name="PTS06",
        description="Status Code",
        min_length=2,
        max_length=2,
    )

    TaxJurisdictionCodeQualifier: Optional[X12ID] = element(
        name="PTS07",
        description="Tax Jurisdiction Code Qualifier",
        min_length=2,
        max_length=2,
    )

    TaxJurisdictionCode: Optional[X12AN] = element(
        name="PTS08",
        description="Tax Jurisdiction Code",
        min_length=1,
        max_length=10,
    )

    Description: Optional[X12AN] = element(
        name="PTS09",
        description="Description",
        min_length=1,
        max_length=80,
    )

    TypeOfTaxingAuthorityCode: Optional[X12ID] = element(
        name="PTS10",
        description="Type of Taxing Authority Code",
        min_length=2,
        max_length=2,
    )

    StatusCode3: Optional[X12ID] = element(
        name="PTS11",
        description="Status Code",
        min_length=2,
        max_length=2,
    )
