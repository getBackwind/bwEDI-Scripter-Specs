# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G61(Segment):
    """
    G61 - Contact
    
    Description:
        To identify a person or office to whom communications should be directed
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G61/
    """
    _id: Literal["G61"] = id_element(name="G61")

    ContactFunctionCode: X12ID = element(
        name="G6101",
        description="Contact Function Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Name: X12AN = element(
        name="G6102",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    CommunicationNumberQualifier: Optional[X12ID] = element(
        name="G6103",
        description="Communication Number Qualifier",
        min_length=2,
        max_length=2,
    )

    CommunicationNumber: Optional[X12AN] = element(
        name="G6104",
        description="Communication Number",
        min_length=1,
        max_length=80,
    )

    ContactInquiryReference: Optional[X12AN] = element(
        name="G6105",
        description="Contact Inquiry Reference",
        min_length=1,
        max_length=20,
    )
