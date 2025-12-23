# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class TXI(Segment):
    """
    TXI - Tax Information
    
    Description:
        To specify tax information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TXI/
    """
    _id: Literal["TXI"] = id_element(name="TXI")

    TaxType: X12ID = element(
        name="TXI01",
        description="Tax Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Amount: Optional[X12R] = element(
        name="TXI02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12R] = element(
        name="TXI03",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    JurisdictionQualifier: Optional[X12ID] = element(
        name="TXI04",
        description="Tax Jurisdiction Code Qualifier",
        min_length=2,
        max_length=2,
    )

    JurisdictionCode: Optional[X12AN] = element(
        name="TXI05",
        description="Tax Jurisdiction Code",
        min_length=1,
        max_length=10,
    )

    TaxExemptCode: Optional[X12ID] = element(
        name="TXI06",
        description="Tax Exempt Code",
        min_length=1,
        max_length=1,
    )

    RelationshipCode: Optional[X12ID] = element(
        name="TXI07",
        description="Relationship Code",
        min_length=1,
        max_length=1,
    )

    DollarBasisForPercent: Optional[X12R] = element(
        name="TXI08",
        description="Dollar Basis For Percent",
        min_length=1,
        max_length=9,
    )

    RegistrationNumber: Optional[X12AN] = element(
        name="TXI09",
        description="Tax Identification Number",
        min_length=1,
        max_length=20,
    )

    Description: Optional[X12AN] = element(
        name="TXI10",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )
