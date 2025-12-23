# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class R2C(Segment):
    """
    R2C - Division Basis
    
    Description:
        To identify the basis for divisions detail for carriers participating in the route
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R2C/
    """
    _id: Literal["R2C"] = id_element(name="R2C")

    DivisionTypeCode: X12ID = element(
        name="R2C01",
        description="Division Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="R2C02",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    FactorAmount: Optional[X12R] = element(
        name="R2C03",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="R2C04",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )
