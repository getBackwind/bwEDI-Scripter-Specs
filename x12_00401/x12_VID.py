# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class VID(Segment):
    """
    VID - Conveyance Identification
    
    Description:
        To identifya conveyance and its attributes
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/VID/
    """
    _id: Literal["VID"] = id_element(name="VID")

    EquipmentDescriptionCode: X12ID = element(
        name="VID01",
        description="Equipment Description Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="VID02",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="VID03",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    SealNumber: Optional[X12AN] = element(
        name="VID04",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    SealNumber2: Optional[X12AN] = element(
        name="VID05",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    EquipmentLength: Optional[X12Nn] = element(
        name="VID06",
        description="Equipment Length",
        min_length=4,
        max_length=5,
    )

    Height: Optional[X12R] = element(
        name="VID07",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="VID08",
        description="Width",
        min_length=1,
        max_length=8,
    )

    EquipmentType: Optional[X12ID] = element(
        name="VID09",
        description="Equipment Type",
        min_length=4,
        max_length=4,
    )

    LoadEmptyStatusCode: Optional[X12ID] = element(
        name="VID10",
        description="Load/Empty Status Code",
        min_length=1,
        max_length=1,
    )

    TypeOfServiceCode: Optional[X12ID] = element(
        name="VID11",
        description="Type of Service Code",
        min_length=2,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="VID12",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="VID13",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
