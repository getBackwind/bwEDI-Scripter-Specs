# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class S1(Segment):
    """
    S1 - Stop-off Name
    
    Description:
        To identify a stop-off party
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/S1/
    """
    _id: Literal["S1"] = id_element(name="S1")

    StopSequenceNumber: X12Nn = element(
        name="S101",
        description="Stop Sequence Number",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    Name30CharacterFormat: X12AN = element(
        name="S102",
        description="Name (30 Character Format)",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="S103",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="S104",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="S105",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    AccomplishCode: X12ID = element(
        name="S106",
        description="Accomplish Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
