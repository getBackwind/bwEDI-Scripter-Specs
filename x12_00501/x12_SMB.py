# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class SMB(Segment):
    """
    SMB - Beginning Segment for Railroad Station Master File
    
    Description:
        To identify the type of transaction update and type of station
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SMB/
    """
    _id: Literal["SMB"] = id_element(name="SMB")

    TransactionSetPurposeCode: X12ID = element(
        name="SMB01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StationTypeCode: X12ID = element(
        name="SMB02",
        description="Station Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="SMB03",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    StationTypeCode2: Optional[X12ID] = element(
        name="SMB04",
        description="Station Type Code",
        min_length=1,
        max_length=1,
    )

    StationTypeCode3: Optional[X12ID] = element(
        name="SMB05",
        description="Station Type Code",
        min_length=1,
        max_length=1,
    )

    StationTypeCode4: Optional[X12ID] = element(
        name="SMB06",
        description="Station Type Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="SMB07",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Rule260JunctionCode: Optional[X12ID] = element(
        name="SMB08",
        description="Rule 260 Junction Code",
        min_length=1,
        max_length=5,
    )

    StationTypeCode5: Optional[X12ID] = element(
        name="SMB09",
        description="Station Type Code",
        min_length=1,
        max_length=1,
    )
