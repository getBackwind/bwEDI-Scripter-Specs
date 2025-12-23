# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class PLD(Segment):
    """
    PLD - Pallet Shipment Information
    
    Description:
        To specify pallet information including quantity, exchange, and weight
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PLD/
    """
    _id: Literal["PLD"] = id_element(name="PLD")

    QuantityOfPalletsShipped: X12Nn = element(
        name="PLD01",
        description="Quantity of Pallets Shipped",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    PalletExchangeCode: Optional[X12ID] = element(
        name="PLD02",
        description="Pallet Exchange Code",
        min_length=1,
        max_length=1,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="PLD03",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="PLD04",
        description="Weight",
        min_length=1,
        max_length=10,
    )
