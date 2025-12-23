# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class H6(Segment):
    """
    H6 - Special Services
    
    Description:
        To identify forms of unitization, liability issues, and special services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/H6/
    """
    _id: Literal["H6"] = id_element(name="H6")

    SpecialServicesCode: Optional[X12ID] = element(
        name="H601",
        description="Special Services Code",
        min_length=2,
        max_length=3,
    )

    SpecialServicesCode2: Optional[X12ID] = element(
        name="H602",
        description="Special Services Code",
        min_length=2,
        max_length=3,
    )

    QuantityOfPalletsShipped: Optional[X12Nn] = element(
        name="H603",
        description="Quantity of Pallets Shipped",
        min_length=1,
        max_length=3,
    )

    PalletExchangeCode: Optional[X12ID] = element(
        name="H604",
        description="Pallet Exchange Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="H605",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="H606",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    PickupOrDeliveryCode: Optional[X12ID] = element(
        name="H607",
        description="Pickup or Delivery Code",
        min_length=1,
        max_length=2,
    )
