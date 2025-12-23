# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class APE(Segment):
    """
    APE - Assurance Protocol Error
    
    Description:
        To report assurance protocol errors in a security structure
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/APE/
    """
    _id: Literal["APE"] = id_element(name="APE")

    BusinessPurposeOfAssurance: X12ID = element(
        name="APE01",
        description="Business Purpose of Assurance",
        mandatory=True,
    )

    DomainOfComputationOfAssurance: X12ID = element(
        name="APE02",
        description="Domain of Computation of Assurance",
        mandatory=True,
    )

    SecurityOrAssuranceProtocolErrorCode: X12ID = element(
        name="APE03",
        description="Security or Assurance Protocol Error Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    AssuranceOriginator: Optional[X12AN] = element(
        name="APE04",
        description="Assurance Originator",
        min_length=1,
        max_length=64,
    )

    AssuranceRecipient: Optional[X12AN] = element(
        name="APE05",
        description="Assurance Recipient",
        min_length=1,
        max_length=64,
    )
