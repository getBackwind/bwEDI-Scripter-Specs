# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SPE(Segment):
    """
    SPE - Security Protocol Error
    
    Description:
        To report security protocol errors in a security structure
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SPE/
    """
    _id: Literal["SPE"] = id_element(name="SPE")

    SecurityOriginatorName: X12AN = element(
        name="SPE01",
        description="Security Originator Name",
        mandatory=True,
        min_length=1,
        max_length=64,
    )

    SecurityRecipientName: X12AN = element(
        name="SPE02",
        description="Security Recipient Name",
        mandatory=True,
        min_length=1,
        max_length=64,
    )

    SecurityTypeCode: X12ID = element(
        name="SPE03",
        description="Security Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    SecurityOrAssuranceProtocolErrorCode: X12ID = element(
        name="SPE04",
        description="Security or Assurance Protocol Error Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )
