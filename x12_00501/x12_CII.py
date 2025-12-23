# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class CII(Segment):
    """
    CII - Conveyance Insurance Information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CII/
    """
    _id: Literal["CII"] = id_element(name="CII")

    Name: X12AN = element(
        name="CII01",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    ReferenceIdentification: X12AN = element(
        name="CII02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Year: X12Nn = element(
        name="CII03",
        description="Year",
        mandatory=True,
        min_length=4,
        max_length=4,
    )

    CurrencyCode: X12ID = element(
        name="CII04",
        description="Currency Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Amount: X12Nn = element(
        name="CII05",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )
