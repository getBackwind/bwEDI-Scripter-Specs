# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class G08(Segment):
    """
    G08 - Pallet Receipt Disposition
    
    Description:
        To indicate quantity, condition, and disposition of pallets received
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G08/
    """
    _id: Literal["G08"] = id_element(name="G08")

    QuantityOfPalletsReceived: Optional[X12Nn] = element(
        name="G0801",
        description="Quantity of Pallets Received",
        min_length=1,
        max_length=3,
    )

    QuantityOfPalletsReturned: Optional[X12Nn] = element(
        name="G0802",
        description="Quantity of Pallets Returned",
        min_length=1,
        max_length=3,
    )

    QuantityContested: Optional[X12R] = element(
        name="G0803",
        description="Quantity Contested",
        min_length=1,
        max_length=7,
    )

    ReceivingConditionCode: Optional[X12ID] = element(
        name="G0804",
        description="Receiving Condition Code",
        min_length=2,
        max_length=2,
    )
