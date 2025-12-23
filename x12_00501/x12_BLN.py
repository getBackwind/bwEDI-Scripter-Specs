# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class BLN(Segment):
    """
    BLN - Balance Information
    
    Description:
        To provide specific balance information for financial account reporting
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BLN/
    """
    _id: Literal["BLN"] = id_element(name="BLN")

    CodeListQualifierCode: X12ID = element(
        name="BLN01",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="BLN02",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    MonetaryAmount: X12R = element(
        name="BLN03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Date: Optional[X12DT] = element(
        name="BLN04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BLN05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="BLN06",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
