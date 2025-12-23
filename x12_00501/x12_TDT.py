# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TDT(Segment):
    """
    TDT - Tax Delinquency Status
    
    Description:
        To specify the tax delinquency status on real property
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TDT/
    """
    _id: Literal["TDT"] = id_element(name="TDT")

    RealEstateTaxDelinquencyTypeCode: X12ID = element(
        name="TDT01",
        description="Real Estate Tax Delinquency Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="TDT02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    StatusCode: Optional[X12ID] = element(
        name="TDT03",
        description="Status Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="TDT04",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
