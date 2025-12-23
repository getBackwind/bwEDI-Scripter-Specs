# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CID(Segment):
    """
    CID - Characteristic/Class ID
    
    Description:
        To specify the general class or specific characteristic upon which test results are being reported or are to be taken
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CID/
    """
    _id: Literal["CID"] = id_element(name="CID")

    MeasurementQualifier: Optional[X12ID] = element(
        name="CID01",
        description="Measurement Qualifier",
        min_length=1,
        max_length=3,
    )

    ProductProcessCharacteristicCode: Optional[X12ID] = element(
        name="CID02",
        description="Product/Process Characteristic Code",
        min_length=2,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="CID03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    ProductDescriptionCode: Optional[X12AN] = element(
        name="CID04",
        description="Product Description Code",
        min_length=1,
        max_length=12,
    )

    Description: Optional[X12AN] = element(
        name="CID05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="CID06",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CID07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
