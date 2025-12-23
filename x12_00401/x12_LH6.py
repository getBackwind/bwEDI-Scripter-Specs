# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LH6(Segment):
    """
    LH6 - Hazardous Certification
    
    Description:
        To specify the name of the person certifying that the shipment complies with the regulations and/or the actual certification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LH6/
    """
    _id: Literal["LH6"] = id_element(name="LH6")

    Name: Optional[X12AN] = element(
        name="LH601",
        description="Name",
        min_length=1,
        max_length=60,
    )

    HazardousCertificationCode: Optional[X12ID] = element(
        name="LH602",
        description="Hazardous Certification Code",
        min_length=1,
        max_length=1,
    )

    HazardousCertificationDeclaration: Optional[X12AN] = element(
        name="LH603",
        description="Hazardous Certification Declaration",
        min_length=1,
        max_length=25,
    )

    HazardousCertificationDeclaration2: Optional[X12AN] = element(
        name="LH604",
        description="Hazardous Certification Declaration",
        min_length=1,
        max_length=25,
    )
