# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SIN(Segment):
    """
    SIN - Substance Use
    
    Description:
        To report use of tobacco, alcohol, drugs or other substances
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SIN/
    """
    _id: Literal["SIN"] = id_element(name="SIN")

    InformationStatusCode: X12ID = element(
        name="SIN01",
        description="Information Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ControlledSubstanceTypeCode: Optional[X12ID] = element(
        name="SIN02",
        description="Controlled Substance Type Code",
        min_length=2,
        max_length=2,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="SIN03",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="SIN04",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="SIN05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
