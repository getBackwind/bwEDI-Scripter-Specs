# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RC(Segment):
    """
    RC - Root Cause
    
    Description:
        To specify the specific part responsible for a customer complaint in a request for service of a product and/or to describe the particular failure mechanism in a failing part or assembly
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RC/
    """
    _id: Literal["RC"] = id_element(name="RC")

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="RC01",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="RC02",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Name: Optional[X12AN] = element(
        name="RC03",
        description="Name",
        min_length=1,
        max_length=60,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="RC04",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="RC05",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    CasualPartConditionCode: Optional[X12AN] = element(
        name="RC06",
        description="Casual Part Condition Code",
        min_length=1,
        max_length=3,
    )

    Description: Optional[X12AN] = element(
        name="RC07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="RC08",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="RC09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
