# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class PEN(Segment):
    """
    PEN - Pension Information
    
    Description:
        To specify financial activity for a pension plan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PEN/
    """
    _id: Literal["PEN"] = id_element(name="PEN")

    TransactionTypeCode: X12ID = element(
        name="PEN01",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PEN02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ContributionCode: Optional[X12ID] = element(
        name="PEN03",
        description="Contribution Code",
        min_length=2,
        max_length=2,
    )

    Percent: Optional[X12R] = element(
        name="PEN04",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    SpecialProcessingType: Optional[X12AN] = element(
        name="PEN05",
        description="Special Processing Type",
        min_length=1,
        max_length=6,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PEN06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Number: Optional[X12Nn] = element(
        name="PEN07",
        description="Number",
        min_length=1,
        max_length=9,
    )

    LoanTypeCode: Optional[X12ID] = element(
        name="PEN08",
        description="Loan Type Code",
        min_length=1,
        max_length=2,
    )

    MaintenanceTypeCode: Optional[X12ID] = element(
        name="PEN09",
        description="Maintenance Type Code",
        min_length=3,
        max_length=3,
    )
