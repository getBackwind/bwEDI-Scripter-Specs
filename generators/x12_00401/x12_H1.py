# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class H1(Segment):
    """
    H1 - Hazardous Material
    
    Description:
        To specify information relative to hazardous material
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/H1/
    """
    _id: Literal["H1"] = id_element(name="H1")

    HazardousMaterialCode: X12AN = element(
        name="H101",
        description="Hazardous Material Code",
        mandatory=True,
        min_length=4,
        max_length=10,
    )

    HazardousMaterialClassCode: Optional[X12AN] = element(
        name="H102",
        description="Hazardous Material Class Code",
        min_length=1,
        max_length=4,
    )

    HazardousMaterialCodeQualifier: Optional[X12ID] = element(
        name="H103",
        description="Hazardous Material Code Qualifier",
        min_length=1,
        max_length=1,
    )

    HazardousMaterialDescription: Optional[X12AN] = element(
        name="H104",
        description="Hazardous Material Description",
        min_length=2,
        max_length=30,
    )

    HazardousMaterialContact: Optional[X12AN] = element(
        name="H105",
        description="Hazardous Material Contact",
        min_length=1,
        max_length=24,
    )

    HazardousMaterialsPage: Optional[X12AN] = element(
        name="H106",
        description="Hazardous Materials Page",
        min_length=1,
        max_length=6,
    )

    FlashpointTemperature: Optional[X12Nn] = element(
        name="H107",
        description="Flashpoint Temperature",
        min_length=1,
        max_length=3,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="H108",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PackingGroupCode: Optional[X12ID] = element(
        name="H109",
        description="Packing Group Code",
        min_length=1,
        max_length=3,
    )
