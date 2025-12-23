# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class OOI(Segment):
    """
    OOI - Associated Object Type Identification
    
    Description:
        To identify attributes and status related to the object
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/OOI/
    """
    _id: Literal["OOI"] = id_element(name="OOI")

    ObjectIdentificationGroup: X12AN = element(
        name="OOI01",
        description="Object Identification Group",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ObjectTypeQualifier: X12ID = element(
        name="OOI02",
        description="Object Type Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ObjectAttributeIdentification: X12AN = element(
        name="OOI03",
        description="Object Attribute Identification",
        mandatory=True,
        min_length=1,
        max_length=256,
    )

    ControllingAgency: Optional[X12ID] = element(
        name="OOI04",
        description="Controlling Agency",
    )
