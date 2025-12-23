# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LS1(Segment):
    """
    LS1 - Asset Item Identification
    
    Description:
        To specify basic asset line item data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LS1/
    """
    _id: Literal["LS1"] = id_element(name="LS1")

    Quantity: X12R = element(
        name="LS101",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="LS102",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    ChangeOrResponseTypeCode: Optional[X12ID] = element(
        name="LS103",
        description="Change or Response Type Code",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="LS104",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="LS105",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="LS106",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="LS107",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
