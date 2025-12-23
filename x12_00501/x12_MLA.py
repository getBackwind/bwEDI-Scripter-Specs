# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class MLA(Segment):
    """
    MLA - Mortgage Loan Audit Information
    
    Description:
        To specify audit information about the loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MLA/
    """
    _id: Literal["MLA"] = id_element(name="MLA")

    ReferenceIdentification: X12AN = element(
        name="MLA01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ContractNumber: X12AN = element(
        name="MLA02",
        description="Contract Number",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    MonetaryAmount: X12R = element(
        name="MLA03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="MLA04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ServiceTypeCode: Optional[X12ID] = element(
        name="MLA05",
        description="Service Type Code",
        min_length=1,
        max_length=2,
    )

    StatusCode: Optional[X12ID] = element(
        name="MLA06",
        description="Status Code",
        min_length=2,
        max_length=2,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="MLA08",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
