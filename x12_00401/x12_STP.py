# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12Nn


class STP(Segment):
    """
    STP - Study Parameters
    
    Description:
        To report study parameters
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/STP/
    """
    _id: Literal["STP"] = id_element(name="STP")

    Date: X12DT = element(
        name="STP01",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    EntityTitle: X12AN = element(
        name="STP02",
        description="Entity Title",
        mandatory=True,
        min_length=1,
        max_length=132,
    )

    ReferenceIdentification: X12AN = element(
        name="STP03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: X12AN = element(
        name="STP04",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Number: X12Nn = element(
        name="STP05",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    Number2: X12Nn = element(
        name="STP06",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    Number3: X12Nn = element(
        name="STP07",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    Number4: Optional[X12Nn] = element(
        name="STP08",
        description="Number",
        min_length=1,
        max_length=9,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="STP09",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
