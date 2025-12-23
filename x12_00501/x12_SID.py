# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class SID(Segment):
    """
    SID - Standard Transportation Commodity Code Identification
    
    Description:
        To convey the Standard Transportation Commodity Code (STCC) and associated descriptions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SID/
    """
    _id: Literal["SID"] = id_element(name="SID")

    CommodityCodeQualifier: X12ID = element(
        name="SID01",
        description="Commodity Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CommodityCode: X12AN = element(
        name="SID02",
        description="Commodity Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SID03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="SID04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    RatingSummaryValueCode: Optional[X12ID] = element(
        name="SID05",
        description="Rating Summary Value Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SID06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
