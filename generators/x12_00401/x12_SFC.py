# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class SFC(Segment):
    """
    SFC - Storage Facility Characteristics
    
    Description:
        To indicate the physical characteristics of any storage facility or area
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SFC/
    """
    _id: Literal["SFC"] = id_element(name="SFC")

    FacilityCharacteristicCodeQualifier: X12ID = element(
        name="SFC01",
        description="Facility Characteristic Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    FacilityCharacteristicCode: X12ID = element(
        name="SFC02",
        description="Facility Characteristic Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )
