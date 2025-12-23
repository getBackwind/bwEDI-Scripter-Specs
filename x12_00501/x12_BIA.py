# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BIA(Segment):
    """
    BIA - Beginning Segment for Inventory Inquiry/Advice
    
    Description:
        To indicate the beginning of an Inventory Inquiry/Advice Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BIA/
    """
    _id: Literal["BIA"] = id_element(name="BIA")

    PurposeCode: X12ID = element(
        name="BIA01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReportTypeCode: X12ID = element(
        name="BIA02",
        description="Report Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RefID: X12AN = element(
        name="BIA03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: X12DT = element(
        name="BIA04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BIA05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ActionCode: Optional[X12ID] = element(
        name="BIA06",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
