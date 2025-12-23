# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BAX(Segment):
    """
    BAX - Beginning Segment for Advance Consist and Transportation Automatic Equipment ID
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BAX/
    """
    _id: Literal["BAX"] = id_element(name="BAX")

    StandardPointLocationCode: X12ID = element(
        name="BAX01",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    TypeOfConsistCode: X12ID = element(
        name="BAX02",
        description="Type of Consist Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DateTimeQualifier: X12ID = element(
        name="BAX03",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Date: X12DT = element(
        name="BAX04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: X12TM = element(
        name="BAX05",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    InterchangeTrainIdentification: Optional[X12AN] = element(
        name="BAX06",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="BAX07",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BAX08",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    DirectionIdentifierCode: Optional[X12ID] = element(
        name="BAX09",
        description="Direction Identifier Code",
        min_length=1,
        max_length=1,
    )

    Date2: Optional[X12DT] = element(
        name="BAX10",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="BAX11",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="BAX12",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BAX13",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ServiceLevelCode: Optional[X12ID] = element(
        name="BAX14",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )
