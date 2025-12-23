# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class ENE(Segment):
    """
    ENE - Electronic Systems Environment
    
    Description:
        To specify electronic systems environment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ENE/
    """
    _id: Literal["ENE"] = id_element(name="ENE")

    CommunicationsEnvironmentCode: X12ID = element(
        name="ENE01",
        description="Communications Environment Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CommunicationNumberQualifier: X12ID = element(
        name="ENE02",
        description="Communication Number Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CommunicationNumber: X12AN = element(
        name="ENE03",
        description="Communication Number",
        mandatory=True,
        min_length=1,
        max_length=256,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="ENE04",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="ENE05",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
