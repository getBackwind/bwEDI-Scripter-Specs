# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class W13(Segment):
    """
    W13 - Item Detail Exception
    
    Description:
        To indicate exceptions to quantities and receiving condition for a specific product
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W13/
    """
    _id: Literal["W13"] = id_element(name="W13")

    Quantity: X12R = element(
        name="W1301",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="W1302",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReceivingConditionCode: X12ID = element(
        name="W1303",
        description="Receiving Condition Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    WarehouseLotNumber: Optional[X12AN] = element(
        name="W1304",
        description="Warehouse Lot Number",
        min_length=1,
        max_length=12,
    )

    DamageReasonCode: Optional[X12ID] = element(
        name="W1305",
        description="Damage Reason Code",
        min_length=2,
        max_length=2,
    )
