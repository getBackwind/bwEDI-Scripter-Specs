# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class AK9(Segment):
    """
    AK9 - Functional Group Response Trailer
    
    Description:
        To acknowledge acceptance or rejection of a functional group and report the number of included transaction sets from the original trailer, the accepted sets, and the received sets in this functional group
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AK9/
    """
    _id: Literal["AK9"] = id_element(name="AK9")

    AcknowledgementCode: X12ID = element(
        name="AK901",
        description="Functional Group Acknowledge Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    TransactionSetsCount: X12Nn = element(
        name="AK902",
        description="Number of Transaction Sets Included",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    ReceivedCount: X12Nn = element(
        name="AK903",
        description="Number of Received Transaction Sets",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    AcceptedCount: X12Nn = element(
        name="AK904",
        description="Number of Accepted Transaction Sets",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    ErrorCode: Optional[X12ID] = element(
        name="AK905",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ErrorCode2: Optional[X12ID] = element(
        name="AK906",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ErrorCode3: Optional[X12ID] = element(
        name="AK907",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ErrorCode4: Optional[X12ID] = element(
        name="AK908",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ErrorCode5: Optional[X12ID] = element(
        name="AK909",
        description="Functional Group Syntax Error Code",
        min_length=1,
        max_length=2,
    )
