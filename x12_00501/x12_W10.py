# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class W10(Segment):
    """
    W10 - Warehouse Additional Carrier Information
    
    Description:
        To transmit shipping information and requirements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W10/
    """
    _id: Literal["W10"] = id_element(name="W10")

    UnitLoadOptionCode: Optional[X12ID] = element(
        name="W1001",
        description="Unit Load Option Code",
        min_length=2,
        max_length=2,
    )

    QuantityOfPalletsShipped: Optional[X12Nn] = element(
        name="W1002",
        description="Quantity of Pallets Shipped",
        min_length=1,
        max_length=3,
    )

    PalletExchangeCode: Optional[X12ID] = element(
        name="W1003",
        description="Pallet Exchange Code",
        min_length=1,
        max_length=1,
    )

    SealNumber: Optional[X12AN] = element(
        name="W1004",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    SealNumber2: Optional[X12AN] = element(
        name="W1005",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    Temperature: Optional[X12R] = element(
        name="W1006",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="W1007",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Temperature2: Optional[X12R] = element(
        name="W1008",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="W1009",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
