# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class ID2(Segment):
    """
    ID2 - Item Image Detail
    
    Description:
        To transmit item image information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ID2/
    """
    _id: Literal["ID2"] = id_element(name="ID2")

    CashRegisterItemDescription: Optional[X12AN] = element(
        name="ID201",
        description="Cash Register Item Description",
        min_length=1,
        max_length=20,
    )

    CashRegisterItemDescription2: Optional[X12AN] = element(
        name="ID202",
        description="Cash Register Item Description",
        min_length=1,
        max_length=20,
    )

    SpaceManagementReferenceCode: Optional[X12ID] = element(
        name="ID203",
        description="Space Management Reference Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ID204",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Name: Optional[X12AN] = element(
        name="ID205",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Name2: Optional[X12AN] = element(
        name="ID206",
        description="Name",
        min_length=1,
        max_length=60,
    )

    SpaceManagementReferenceCode2: Optional[X12ID] = element(
        name="ID207",
        description="Space Management Reference Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="ID208",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
