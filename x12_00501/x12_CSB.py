# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CSB(Segment):
    """
    CSB - Cryptographic Service Message Body
    
    Description:
        To provide a mechanism for carrying a field tag and its associated contents from an ANSI X9.17 cryptographic service message (CSM) in an X12 format
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CSB/
    """
    _id: Literal["CSB"] = id_element(name="CSB")

    CryptographicServiceMessageCSMFieldTag: X12ID = element(
        name="CSB01",
        description="Cryptographic Service Message (CSM) Field Tag",
        mandatory=True,
    )

    CryptographicServiceMessageCSMFieldContents: Optional[X12AN] = element(
        name="CSB02",
        description="Cryptographic Service Message (CSM) Field Contents",
        min_length=1,
        max_length=32,
    )
