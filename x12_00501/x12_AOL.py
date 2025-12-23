# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class AOL(Segment):
    """
    AOL - Animal Observation Location
    
    Description:
        To report the location of a specific observation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AOL/
    """
    _id: Literal["AOL"] = id_element(name="AOL")

    ObservationTypeCode: X12ID = element(
        name="AOL01",
        description="Observation Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Description: X12AN = element(
        name="AOL02",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )

    TissueOrSpecimenDispositionCode: Optional[X12ID] = element(
        name="AOL03",
        description="Tissue or Specimen Disposition Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="AOL04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    SubLocation: Optional[X12AN] = element(
        name="AOL05",
        description="Sub-Location",
        min_length=1,
        max_length=24,
    )

    SubLocation2: Optional[X12AN] = element(
        name="AOL06",
        description="Sub-Location",
        min_length=1,
        max_length=24,
    )

    SubLocation3: Optional[X12AN] = element(
        name="AOL07",
        description="Sub-Location",
        min_length=1,
        max_length=24,
    )

    SurfaceLayerPositionCode: Optional[X12ID] = element(
        name="AOL08",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )
