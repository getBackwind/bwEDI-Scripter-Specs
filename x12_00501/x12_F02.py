# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class F02(Segment):
    """
    F02 - Identification of Shipment
    
    Description:
        To specify date of shipment, carrier, equipment, and carrier's reference number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/F02/
    """
    _id: Literal["F02"] = id_element(name="F02")

    Date: Optional[X12DT] = element(
        name="F0201",
        description="Date",
        min_length=8,
        max_length=8,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="F0202",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="F0203",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="F0204",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="F0205",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="F0206",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="F0207",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    VesselCode: Optional[X12ID] = element(
        name="F0208",
        description="Vessel Code",
        min_length=1,
        max_length=8,
    )

    VesselName: Optional[X12AN] = element(
        name="F0209",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )
