# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class RYL(Segment):
    """
    RYL - Royalty Payment
    
    Description:
        To specify remittance information about royalty payments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RYL/
    """
    _id: Literal["RYL"] = id_element(name="RYL")

    AssignedNumber: X12Nn = element(
        name="RYL01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    NameLastOrOrganizationName: Optional[X12AN] = element(
        name="RYL02",
        description="Name Last or Organization Name",
        min_length=1,
        max_length=35,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="RYL03",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="RYL04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
