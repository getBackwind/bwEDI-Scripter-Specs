# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class R11(Segment):
    """
    R11 - Beginning Segment for Trailer or Container Repair Billing
    
    Description:
        To indicate the start of the Trailer or Container Repair Billing Transaction Set and to identify the billing parties and associated information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R11/
    """
    _id: Literal["R11"] = id_element(name="R11")

    TransactionTypeCode: X12ID = element(
        name="R1101",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="R1102",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: X12ID = element(
        name="R1103",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    InvoiceNumber: X12AN = element(
        name="R1104",
        description="Invoice Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    MonthOfTheYearCode: X12ID = element(
        name="R1105",
        description="Month of the Year Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Year: Optional[X12Nn] = element(
        name="R1106",
        description="Year",
        min_length=4,
        max_length=4,
    )

    TermsTypeCode: Optional[X12ID] = element(
        name="R1107",
        description="Terms Type Code",
        min_length=2,
        max_length=2,
    )
