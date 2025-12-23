# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BAA(Segment):
    """
    BAA - Beginning Segment for Product Transfer Account Adjustment
    
    Description:
        To identify the beginning of a Product Transfer Account Adjustment Transaction Set and further define the type of product account adjustment transaction set and its reference number and date
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BAA/
    """
    _id: Literal["BAA"] = id_element(name="BAA")

    TransactionSetPurposeCode: X12ID = element(
        name="BAA01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: X12ID = element(
        name="BAA02",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BAA03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="BAA04",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BAA05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Time: Optional[X12TM] = element(
        name="BAA06",
        description="Time",
        min_length=4,
        max_length=8,
    )
