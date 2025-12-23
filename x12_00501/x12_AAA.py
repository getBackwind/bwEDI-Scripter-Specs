# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class AAA(Segment):
    """
    AAA - Request Validation
    
    Description:
        To specify the validity of the request and indicate follow-up action authorized
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AAA/
    """
    _id: Literal["AAA"] = id_element(name="AAA")

    YesNoConditionOrResponseCode: X12ID = element(
        name="AAA01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="AAA02",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    RejectReasonCode: Optional[X12ID] = element(
        name="AAA03",
        description="Reject Reason Code",
        min_length=2,
        max_length=2,
    )

    FollowUpActionCode: Optional[X12ID] = element(
        name="AAA04",
        description="Follow-up Action Code",
        min_length=1,
        max_length=1,
    )
