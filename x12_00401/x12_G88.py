# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT


class G88(Segment):
    """
    G88 - Delivery/Return Identification Adjustment
    
    Description:
        To transmit adjustments for identification data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G88/
    """
    _id: Literal["G88"] = id_element(name="G88")

    PhysicalDeliveryOrReturnDate: Optional[X12DT] = element(
        name="G8801",
        description="Physical Delivery or Return Date",
        min_length=8,
        max_length=8,
    )

    ProductOwnershipTransferDate: Optional[X12DT] = element(
        name="G8802",
        description="Product Ownership Transfer Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="G8803",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    PurchaseOrderDate: Optional[X12DT] = element(
        name="G8804",
        description="Purchase Order Date",
        min_length=8,
        max_length=8,
    )

    ReceiverSLocationNumber: Optional[X12AN] = element(
        name="G8805",
        description="Receiver's Location Number",
        min_length=1,
        max_length=6,
    )
