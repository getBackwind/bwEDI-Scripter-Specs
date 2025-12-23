# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class S4A(Segment):
    """
    S4A - Assurance Header Level 2
    
    Description:
        To allow for multiple assurances at the ST/SE level
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/S4A/
    """
    _id: Literal["S4A"] = id_element(name="S4A")

    SecurityVersionReleaseIdentifierCode: X12ID = element(
        name="S4A01",
        description="Security Version/Release Identifier Code",
        mandatory=True,
    )

    BusinessPurposeOfAssurance: X12ID = element(
        name="S4A02",
        description="Business Purpose of Assurance",
        mandatory=True,
    )

    DomainOfComputationOfAssurance: X12ID = element(
        name="S4A04",
        description="Domain of Computation of Assurance",
        mandatory=True,
    )

    AssuranceOriginator: Optional[X12AN] = element(
        name="S4A05",
        description="Assurance Originator",
        min_length=1,
        max_length=64,
    )

    AssuranceRecipient: Optional[X12AN] = element(
        name="S4A06",
        description="Assurance Recipient",
        min_length=1,
        max_length=64,
    )

    AssuranceReferenceNumber: Optional[X12AN] = element(
        name="S4A07",
        description="Assurance Reference Number",
        min_length=1,
        max_length=35,
    )

    DateTimeStamp: Optional[X12AN] = element(
        name="S4A08",
        description="Date Time Stamp",
        min_length=17,
        max_length=25,
    )

    AssuranceText: Optional[X12AN] = element(
        name="S4A09",
        description="Assurance Text",
        min_length=1,
        max_length=64,
    )
