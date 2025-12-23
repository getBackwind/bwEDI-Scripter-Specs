# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R


class BTA(Segment):
    """
    BTA - Beginning Tax Acknowledgment
    
    Description:
        To acknowledge acceptance or rejection of a transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BTA/
    """
    _id: Literal["BTA"] = id_element(name="BTA")

    AcknowledgmentType: X12ID = element(
        name="BTA01",
        description="Acknowledgment Type",
        mandatory=True,
    )

    Date: Optional[X12DT] = element(
        name="BTA02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="BTA03",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="BTA04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
