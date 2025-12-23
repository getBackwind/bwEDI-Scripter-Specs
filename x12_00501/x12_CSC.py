# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class CSC(Segment):
    """
    CSC - Cryptographic Service Message Certificates and Keys
    
    Description:
        To provide a mechanism for exchanging certificates of authority, public keys and associated information in an X12 format
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CSC/
    """
    _id: Literal["CSC"] = id_element(name="CSC")

    CryptographicManagementPurpose: X12ID = element(
        name="CSC01",
        description="Cryptographic Management Purpose",
        mandatory=True,
    )

    SecurityOriginatorName: Optional[X12AN] = element(
        name="CSC02",
        description="Security Originator Name",
        min_length=1,
        max_length=64,
    )

    SecurityRecipientName: Optional[X12AN] = element(
        name="CSC03",
        description="Security Recipient Name",
        min_length=1,
        max_length=64,
    )

    FilterIDCode: Optional[X12ID] = element(
        name="CSC06",
        description="Filter ID Code",
        min_length=3,
        max_length=3,
    )

    VersionIdentifier: Optional[X12AN] = element(
        name="CSC07",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    LengthOfData: Optional[X12Nn] = element(
        name="CSC08",
        description="Length of Data",
        min_length=1,
        max_length=18,
    )
