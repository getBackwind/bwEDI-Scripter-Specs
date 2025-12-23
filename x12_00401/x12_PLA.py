# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12TM


class PLA(Segment):
    """
    PLA - Place or Location
    
    Description:
        To indicate action to be taken for the location specified and to qualify the location specified
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PLA/
    """
    _id: Literal["PLA"] = id_element(name="PLA")

    ActionCode: X12ID = element(
        name="PLA01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    EntityIdentifierCode: X12ID = element(
        name="PLA02",
        description="Entity Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    Date: X12DT = element(
        name="PLA03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="PLA04",
        description="Time",
        min_length=4,
        max_length=8,
    )

    MaintenanceReasonCode: Optional[X12ID] = element(
        name="PLA05",
        description="Maintenance Reason Code",
        min_length=2,
        max_length=2,
    )
