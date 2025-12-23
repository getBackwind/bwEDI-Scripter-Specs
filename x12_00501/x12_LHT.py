# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class LHT(Segment):
    """
    LHT - Transborder Hazardous Requirements
    
    Description:
        To specify the placard information required by the second government agency when shipment is to cross into another country
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LHT/
    """
    _id: Literal["LHT"] = id_element(name="LHT")

    HazardousClassification: Optional[X12ID] = element(
        name="LHT01",
        description="Hazardous Classification",
        min_length=1,
        max_length=30,
    )

    HazardousPlacardNotation: Optional[X12ID] = element(
        name="LHT02",
        description="Hazardous Placard Notation",
        min_length=14,
        max_length=40,
    )

    HazardousEndorsement: Optional[X12ID] = element(
        name="LHT03",
        description="Hazardous Endorsement",
        min_length=4,
        max_length=25,
    )
