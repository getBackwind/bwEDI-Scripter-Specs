# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class ID(Segment):
    """
    ID - Inspection Detail Segment
    
    Description:
        To report the inspection results on automotive vehicles
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ID/
    """
    _id: Literal["ID"] = id_element(name="ID")

    DamageAreaCode: X12ID = element(
        name="ID01",
        description="Damage Area Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DamageTypeCode: X12ID = element(
        name="ID02",
        description="Damage Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DamageSeverityCode: X12ID = element(
        name="ID03",
        description="Damage Severity Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
