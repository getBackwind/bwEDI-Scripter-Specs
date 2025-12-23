# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class F13(Segment):
    """
    F13 - Payment Information
    
    Description:
        To transmit check number and amount information associated with a remittance
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/F13/
    """
    _id: Literal["F13"] = id_element(name="F13")

    CheckNumber: X12AN = element(
        name="F1301",
        description="Check Number",
        mandatory=True,
        min_length=1,
        max_length=16,
    )

    Date: X12DT = element(
        name="F1302",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Amount: X12Nn = element(
        name="F1303",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    MICRNumber: Optional[X12AN] = element(
        name="F1304",
        description="MICR Number",
        min_length=16,
        max_length=16,
    )

    Date2: Optional[X12DT] = element(
        name="F1305",
        description="Date",
        min_length=8,
        max_length=8,
    )

    CurrencyCode: X12ID = element(
        name="F1306",
        description="Currency Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )
