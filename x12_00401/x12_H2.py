# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class H2(Segment):
    """
    H2 - Additional Hazardous Material Description
    
    Description:
        To specify free-form hazardous material descriptive data in addition to the information provided in the H1 segment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/H2/
    """
    _id: Literal["H2"] = id_element(name="H2")

    HazardousMaterialDescription: X12AN = element(
        name="H201",
        description="Hazardous Material Description",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    HazardousMaterialClassification: Optional[X12AN] = element(
        name="H202",
        description="Hazardous Material Classification",
        min_length=1,
        max_length=30,
    )
