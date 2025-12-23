# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class FDA(Segment):
    """
    FDA - Facility Description
    
    Description:
        To specify facility description and ownership rights in regard to facility
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FDA/
    """
    _id: Literal["FDA"] = id_element(name="FDA")

    PropertyOwnershipRightsCode: Optional[X12ID] = element(
        name="FDA01",
        description="Property Ownership Rights Code",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="FDA02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    TypeOfRealEstateAssetCode: Optional[X12ID] = element(
        name="FDA03",
        description="Type of Real Estate Asset Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="FDA04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="FDA05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="FDA06",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )

    ConstructionType: Optional[X12ID] = element(
        name="FDA07",
        description="Construction Type",
    )

    ConstructionType2: Optional[X12ID] = element(
        name="FDA08",
        description="Construction Type",
    )

    Description2: Optional[X12AN] = element(
        name="FDA09",
        description="Description",
        min_length=1,
        max_length=80,
    )
