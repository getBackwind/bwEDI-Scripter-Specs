# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class SSS(Segment):
    """
    SSS - Special Services
    
    Description:
        To specify special conditions or services associated with the purchased product
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SSS/
    """
    _id: Literal["SSS"] = id_element(name="SSS")

    AllowanceOrChargeIndicator: X12ID = element(
        name="SSS01",
        description="Allowance or Charge Indicator",
        mandatory=True,
    )

    AgencyQualifierCode: X12ID = element(
        name="SSS02",
        description="Agency Qualifier Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    SpecialServicesCode: X12ID = element(
        name="SSS03",
        description="Special Services Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ServiceMarksAndNumbers: Optional[X12AN] = element(
        name="SSS04",
        description="Service Marks and Numbers",
        min_length=1,
        max_length=45,
    )

    AllowanceOrChargeRate: Optional[X12R] = element(
        name="SSS05",
        description="Allowance or Charge Rate",
        min_length=1,
        max_length=15,
    )

    Amount: Optional[X12Nn] = element(
        name="SSS06",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="SSS07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Quantity: Optional[X12R] = element(
        name="SSS08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="SSS09",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )
