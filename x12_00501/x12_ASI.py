# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class ASI(Segment):
    """
    ASI - Action or Status Indicator
    
    Description:
        To indicate the action to be taken with the information provided or the status of the entity described
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ASI/
    """
    _id: Literal["ASI"] = id_element(name="ASI")

    ActionCode: X12ID = element(
        name="ASI01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    MaintenanceTypeCode: X12ID = element(
        name="ASI02",
        description="Maintenance Type Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="ASI03",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )
