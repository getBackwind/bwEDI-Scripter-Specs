# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PBI(Segment):
    """
    PBI - Problem Identification
    
    Description:
        To identify an error or previously transmitted error
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PBI/
    """
    _id: Literal["PBI"] = id_element(name="PBI")

    ReferenceIdentification: Optional[X12AN] = element(
        name="PBI01",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ActionCode: Optional[X12ID] = element(
        name="PBI02",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="PBI03",
        description="Free-form Message Text",
        min_length=1,
        max_length=264,
    )

    TaxInformationIdentificationNumber: Optional[X12AN] = element(
        name="PBI04",
        description="Tax Information Identification Number",
        min_length=1,
        max_length=30,
    )

    Quantity: Optional[X12R] = element(
        name="PBI05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    FixedFormatInformation: Optional[X12AN] = element(
        name="PBI06",
        description="Fixed Format Information",
        min_length=1,
        max_length=80,
    )

    Quantity2: Optional[X12R] = element(
        name="PBI07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    FixedFormatInformation2: Optional[X12AN] = element(
        name="PBI08",
        description="Fixed Format Information",
        min_length=1,
        max_length=80,
    )
