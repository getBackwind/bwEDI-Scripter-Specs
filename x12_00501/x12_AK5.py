# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class AK5(Segment):
    """
    AK5 - Transaction Set Response Trailer
    
    Description:
        To acknowledge acceptance or rejection and report errors in a transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AK5/
    """
    _id: Literal["AK5"] = id_element(name="AK5")

    AcknowledgementCode: X12ID = element(
        name="AK501",
        description="Transaction Set Acknowledgment Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ErrorCode: Optional[X12ID] = element(
        name="AK502",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ErrorCode2: Optional[X12ID] = element(
        name="AK503",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ErrorCode3: Optional[X12ID] = element(
        name="AK504",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ErrorCode4: Optional[X12ID] = element(
        name="AK505",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ErrorCode5: Optional[X12ID] = element(
        name="AK506",
        description="Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )
