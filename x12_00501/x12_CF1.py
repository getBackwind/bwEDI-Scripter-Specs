# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class CF1(Segment):
    """
    CF1 - Beginning Segment for Summary Freight Bill Manifest
    
    Description:
        To transmit identifying numbers, dates, and other basic data related to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CF1/
    """
    _id: Literal["CF1"] = id_element(name="CF1")

    MasterReferenceLinkNumber: X12AN = element(
        name="CF101",
        description="Master Reference (Link) Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="CF102",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Date: Optional[X12DT] = element(
        name="CF103",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Count: Optional[X12Nn] = element(
        name="CF104",
        description="Count",
        min_length=1,
        max_length=9,
    )

    Amount: Optional[X12Nn] = element(
        name="CF105",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Date2: Optional[X12DT] = element(
        name="CF106",
        description="Date",
        min_length=8,
        max_length=8,
    )
