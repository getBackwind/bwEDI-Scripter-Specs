# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class COM(Segment):
    """
    COM - Communication Contact Information
    
    Description:
        To specify a communication contact number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/COM/
    """
    _id: Literal["COM"] = id_element(name="COM")

    CommunicationNumberQualifier: X12ID = element(
        name="COM01",
        description="Communication Number Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CommunicationNumber: X12AN = element(
        name="COM02",
        description="Communication Number",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
