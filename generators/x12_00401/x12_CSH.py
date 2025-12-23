# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class CSH(Segment):
    """
    CSH - Sales Requirements
    
    Description:
        To specify general conditions or requirements of the sale
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CSH/
    """
    _id: Literal["CSH"] = id_element(name="CSH")

    RequirementCode: Optional[X12ID] = element(
        name="CSH01",
        description="Sales Requirement Code",
        min_length=1,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="CSH02",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="CSH03",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    AccountNumber: Optional[X12AN] = element(
        name="CSH04",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    Date: Optional[X12DT] = element(
        name="CSH05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="CSH06",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SpecialServicesCode: Optional[X12ID] = element(
        name="CSH07",
        description="Special Services Code",
        min_length=2,
        max_length=3,
    )

    ProductServiceSubstitutionCode: Optional[X12ID] = element(
        name="CSH08",
        description="Product/Service Substitution Code",
        min_length=1,
        max_length=2,
    )

    Percent: Optional[X12R] = element(
        name="CSH09",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    PercentQualifier: Optional[X12ID] = element(
        name="CSH10",
        description="Percent Qualifier",
        min_length=1,
        max_length=2,
    )
