# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class V5(Segment):
    """
    V5 - Vessel Identification
    
    Description:
        To specify vessel code
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/V5/
    """
    _id: Literal["V5"] = id_element(name="V5")

    VesselCodeQualifier: X12ID = element(
        name="V501",
        description="Vessel Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    VesselCode: X12ID = element(
        name="V502",
        description="Vessel Code",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    CountryCode: X12ID = element(
        name="V503",
        description="Country Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )
