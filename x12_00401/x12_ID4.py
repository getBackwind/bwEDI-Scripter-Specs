# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class ID4(Segment):
    """
    ID4 - Load Details
    
    Description:
        To identify shipment details that may impact the rates requested
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ID4/
    """
    _id: Literal["ID4"] = id_element(name="ID4")

    DeclaredValue: Optional[X12Nn] = element(
        name="ID401",
        description="Declared Value",
        min_length=2,
        max_length=12,
    )

    PickUpOrDeliveryCode: Optional[X12ID] = element(
        name="ID402",
        description="Pick-up or Delivery Code",
    )

    WeightQualifier: Optional[X12ID] = element(
        name="ID403",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="ID404",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="ID405",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="ID406",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    Number: Optional[X12Nn] = element(
        name="ID407",
        description="Number",
        min_length=1,
        max_length=9,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="ID408",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="ID409",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
