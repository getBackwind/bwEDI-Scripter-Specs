# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class REC(Segment):
    """
    REC - Real Estate Condition
    
    Description:
        To indicate the condition of real estate property and, if applicable, the actions needed to correct damage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/REC/
    """
    _id: Literal["REC"] = id_element(name="REC")

    OccupancyCode: X12ID = element(
        name="REC01",
        description="Occupancy Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RealEstatePropertyConditionCode: Optional[X12ID] = element(
        name="REC02",
        description="Real Estate Property Condition Code",
        min_length=2,
        max_length=2,
    )

    PropertyDamageCode: Optional[X12ID] = element(
        name="REC03",
        description="Property Damage Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="REC04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="REC05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PropertyInspectionQualifier: Optional[X12ID] = element(
        name="REC06",
        description="Property Inspection Qualifier",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="REC07",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="REC08",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity2: Optional[X12R] = element(
        name="REC09",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    OccupancyVerificationCode: Optional[X12ID] = element(
        name="REC11",
        description="Occupancy Verification Code",
        min_length=2,
        max_length=2,
    )

    NoteReferenceCode: Optional[X12ID] = element(
        name="REC12",
        description="Note Reference Code",
        min_length=3,
        max_length=3,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="REC13",
        description="Free-form Message",
        min_length=1,
        max_length=60,
    )
