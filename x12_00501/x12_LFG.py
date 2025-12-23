# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LFG(Segment):
    """
    LFG - Hazardous Information, Finished Goods
    
    Description:
        To describe hazardous material information for finished goods
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LFG/
    """
    _id: Literal["LFG"] = id_element(name="LFG")

    Description: X12AN = element(
        name="LFG01",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )

    HazardousClassification: X12ID = element(
        name="LFG02",
        description="Hazardous Classification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    UNNAIdentificationCode: X12ID = element(
        name="LFG03",
        description="UN/NA Identification Code",
        mandatory=True,
        min_length=6,
        max_length=6,
    )

    HazardousPlacardNotation: X12ID = element(
        name="LFG04",
        description="Hazardous Placard Notation",
        mandatory=True,
        min_length=14,
        max_length=40,
    )

    PackingGroupCode: Optional[X12ID] = element(
        name="LFG05",
        description="Packing Group Code",
        min_length=1,
        max_length=3,
    )

    HazardousMaterialRegulationsExceptionCode: Optional[X12ID] = element(
        name="LFG06",
        description="Hazardous Material Regulations Exception Code",
        min_length=1,
        max_length=1,
    )
