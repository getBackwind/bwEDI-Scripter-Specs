# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PER(Segment):
    """
    PER - Administrative Communications Contact
    
    Description:
        To identify a person or office to whom administrative communications should be directed
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PER/
    """
    _id: Literal["PER"] = id_element(name="PER")

    ContactTypeCode: X12ID = element(
        name="PER01",
        description="Contact Function Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Name: Optional[X12AN] = element(
        name="PER02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    CommunicationTypeCode: Optional[X12ID] = element(
        name="PER03",
        description="Communication Number Qualifier",
        min_length=2,
        max_length=2,
    )

    CommunicationNumber: Optional[X12AN] = element(
        name="PER04",
        description="Communication Number",
        min_length=1,
        max_length=256,
    )

    CommunicationTypeCode2: Optional[X12ID] = element(
        name="PER05",
        description="Communication Number Qualifier",
        min_length=2,
        max_length=2,
    )

    CommunicationNumber2: Optional[X12AN] = element(
        name="PER06",
        description="Communication Number",
        min_length=1,
        max_length=256,
    )

    CommunicationTypeCode3: Optional[X12ID] = element(
        name="PER07",
        description="Communication Number Qualifier",
        min_length=2,
        max_length=2,
    )

    CommunicationNumber3: Optional[X12AN] = element(
        name="PER08",
        description="Communication Number",
        min_length=1,
        max_length=256,
    )

    ContactInquiryReference: Optional[X12AN] = element(
        name="PER09",
        description="Contact Inquiry Reference",
        min_length=1,
        max_length=20,
    )
