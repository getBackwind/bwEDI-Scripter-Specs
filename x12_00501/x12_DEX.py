# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class DEX(Segment):
    """
    DEX - Delivery Execution Information
    
    Description:
        To provide loan delivery and contract information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DEX/
    """
    _id: Literal["DEX"] = id_element(name="DEX")

    SalesTermsCode: Optional[X12ID] = element(
        name="DEX01",
        description="Sales Terms Code",
        min_length=2,
        max_length=2,
    )

    RemittanceTypeCode: Optional[X12ID] = element(
        name="DEX02",
        description="Remittance Type Code",
        min_length=2,
        max_length=2,
    )

    InvestorOwnershipTypeCode: Optional[X12ID] = element(
        name="DEX03",
        description="Investor Ownership Type Code",
        min_length=1,
        max_length=1,
    )

    Number: Optional[X12Nn] = element(
        name="DEX04",
        description="Number",
        min_length=1,
        max_length=9,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="DEX05",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="DEX06",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
