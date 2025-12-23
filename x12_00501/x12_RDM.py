# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RDM(Segment):
    """
    RDM - Remittance Delivery Method
    
    Description:
        To identify remittance delivery when remittance is separate from payment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RDM/
    """
    _id: Literal["RDM"] = id_element(name="RDM")

    ReportTransmissionCode: X12ID = element(
        name="RDM01",
        description="Report Transmission Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Name: Optional[X12AN] = element(
        name="RDM02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    CommunicationNumber: Optional[X12AN] = element(
        name="RDM03",
        description="Communication Number",
        min_length=1,
        max_length=256,
    )
