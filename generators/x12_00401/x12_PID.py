# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PID(Segment):
    """
    PID - Product/Item Description
    
    Description:
        To describe a product or process in coded or free-form format
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PID/
    """
    _id: Literal["PID"] = id_element(name="PID")

    DescriptionType: X12ID = element(
        name="PID01",
        description="Item Description Type",
        mandatory=True,
    )

    CharCode: Optional[X12ID] = element(
        name="PID02",
        description="Product/Process Characteristic Code",
        min_length=2,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="PID03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    ProductDescriptionCode: Optional[X12AN] = element(
        name="PID04",
        description="Product Description Code",
        min_length=1,
        max_length=12,
    )

    Description: Optional[X12AN] = element(
        name="PID05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    SurfaceLayerPositionCode: Optional[X12ID] = element(
        name="PID06",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="PID07",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PID08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    LanguageCode: Optional[X12ID] = element(
        name="PID09",
        description="Language Code",
        min_length=2,
        max_length=3,
    )
