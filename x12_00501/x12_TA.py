# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TA(Segment):
    """
    TA - Tax Authority
    
    Description:
        To identify a jurisdiction's taxing authority
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TA/
    """
    _id: Literal["TA"] = id_element(name="TA")

    TaxJurisdictionCodeQualifier: Optional[X12ID] = element(
        name="TA01",
        description="Tax Jurisdiction Code Qualifier",
        min_length=2,
        max_length=2,
    )

    TaxJurisdictionCode: Optional[X12AN] = element(
        name="TA02",
        description="Tax Jurisdiction Code",
        min_length=1,
        max_length=10,
    )

    Description: Optional[X12AN] = element(
        name="TA03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    TypeOfTaxingAuthorityCode: Optional[X12ID] = element(
        name="TA04",
        description="Type of Taxing Authority Code",
        min_length=2,
        max_length=2,
    )

    Description2: Optional[X12AN] = element(
        name="TA05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    TaxServicePaymentCode: Optional[X12ID] = element(
        name="TA06",
        description="Tax Service Payment Code",
        min_length=1,
        max_length=1,
    )

    StatusCode: Optional[X12ID] = element(
        name="TA07",
        description="Status Code",
        min_length=2,
        max_length=2,
    )
