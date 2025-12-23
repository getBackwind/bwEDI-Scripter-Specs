# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class VDI(Segment):
    """
    VDI - Value Description or Information
    
    Description:
        To provide detailed description of a financial value
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/VDI/
    """
    _id: Literal["VDI"] = id_element(name="VDI")

    CodeCategory: Optional[X12ID] = element(
        name="VDI01",
        description="Code Category",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="VDI03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Percent: Optional[X12R] = element(
        name="VDI04",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="VDI05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Number: Optional[X12Nn] = element(
        name="VDI06",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number2: Optional[X12Nn] = element(
        name="VDI07",
        description="Number",
        min_length=1,
        max_length=9,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="VDI08",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="VDI09",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="VDI10",
        description="Unit of Time Period or Interval",
    )

    Quantity2: Optional[X12R] = element(
        name="VDI11",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Multiplier: Optional[X12R] = element(
        name="VDI12",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    RoundingSystemCode: Optional[X12ID] = element(
        name="VDI13",
        description="Rounding System Code",
        min_length=1,
        max_length=1,
    )

    LoanPaymentTypeCode: Optional[X12ID] = element(
        name="VDI14",
        description="Loan Payment Type Code",
        min_length=2,
        max_length=2,
    )

    LoanPaymentTypeCode2: Optional[X12ID] = element(
        name="VDI15",
        description="Loan Payment Type Code",
        min_length=2,
        max_length=2,
    )
