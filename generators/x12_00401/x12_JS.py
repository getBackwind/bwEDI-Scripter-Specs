# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class JS(Segment):
    """
    JS - Rail Junction Settlement Role Information
    
    Description:
        To define the interchange carriers and their roles
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/JS/
    """
    _id: Literal["JS"] = id_element(name="JS")

    StandardCarrierAlphaCode: X12ID = element(
        name="JS01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    RailJunctionSettlementRoleCode: X12ID = element(
        name="JS02",
        description="Rail Junction Settlement Role Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode2: X12ID = element(
        name="JS03",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    RailJunctionSettlementRoleCode2: X12ID = element(
        name="JS04",
        description="Rail Junction Settlement Role Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
