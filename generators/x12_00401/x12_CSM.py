# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CSM(Segment):
    """
    CSM - Cryptographic Service Message Header
    
    Description:
        To indicate the beginning of a Cryptographic Service Message (CSM) Transaction Set and to provide both the class or type of the CSM and the cryptographic end parties to the transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CSM/
    """
    _id: Literal["CSM"] = id_element(name="CSM")

    CryptographicServiceMessageCSMMessageClassCode: X12ID = element(
        name="CSM01",
        description="Cryptographic Service Message (CSM) Message Class Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    SecurityOriginatorName: Optional[X12AN] = element(
        name="CSM02",
        description="Security Originator Name",
        min_length=1,
        max_length=64,
    )

    SecurityRecipientName: Optional[X12AN] = element(
        name="CSM03",
        description="Security Recipient Name",
        min_length=1,
        max_length=64,
    )
