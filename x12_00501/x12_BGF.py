# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BGF(Segment):
    """
    BGF - Beginning Segment for File Transfer Information
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BGF/
    """
    _id: Literal["BGF"] = id_element(name="BGF")

    TransactionSetIdentifierCode: Optional[X12ID] = element(
        name="BGF01",
        description="Transaction Set Identifier Code",
        min_length=3,
        max_length=3,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="BGF02",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="BGF03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )
