# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn


class GH(Segment):
    """
    GH - Group Header
    
    Description:
        To indicate the list identity for the details following
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/GH/
    """
    _id: Literal["GH"] = id_element(name="GH")

    TransactionSetPurposeCode: X12ID = element(
        name="GH01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="GH02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    NumberOfLineItems: Optional[X12Nn] = element(
        name="GH03",
        description="Number of Line Items",
        min_length=1,
        max_length=6,
    )

    RevisionNumber: Optional[X12Nn] = element(
        name="GH04",
        description="Revision Number",
        min_length=1,
        max_length=4,
    )
