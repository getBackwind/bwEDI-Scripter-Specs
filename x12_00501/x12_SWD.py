# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class SWD(Segment):
    """
    SWD - Switching Details
    
    Description:
        To transmit data relating to the details of the switching service being performed.
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SWD/
    """
    _id: Literal["SWD"] = id_element(name="SWD")

    InvoiceNumber: Optional[X12AN] = element(
        name="SWD01",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    Weight: Optional[X12R] = element(
        name="SWD02",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    TariffApplicationCode: Optional[X12ID] = element(
        name="SWD03",
        description="Tariff Application Code",
        min_length=1,
        max_length=1,
    )

    ApplicationErrorConditionCode: Optional[X12ID] = element(
        name="SWD04",
        description="Application Error Condition Code",
        min_length=1,
        max_length=3,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SWD05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SWD06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    IndustryCode: Optional[X12AN] = element(
        name="SWD07",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Number: Optional[X12Nn] = element(
        name="SWD08",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number2: Optional[X12Nn] = element(
        name="SWD09",
        description="Number",
        min_length=1,
        max_length=9,
    )
