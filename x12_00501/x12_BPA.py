# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BPA(Segment):
    """
    BPA - Beginning Segment for Price Authorization Acknowledgment/Status
    
    Description:
        To identify the beginning of a Price Authorization Acknowledgment/Status Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BPA/
    """
    _id: Literal["BPA"] = id_element(name="BPA")

    TransactionSetPurposeCode: X12ID = element(
        name="BPA01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BPA02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="BPA03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BPA04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Time: Optional[X12TM] = element(
        name="BPA05",
        description="Time",
        min_length=4,
        max_length=8,
    )
