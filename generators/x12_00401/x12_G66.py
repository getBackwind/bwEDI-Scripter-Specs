# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G66(Segment):
    """
    G66 - Transportation Instructions
    
    Description:
        To specify transportation instructions relating to the shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G66/
    """
    _id: Literal["G66"] = id_element(name="G66")

    ShipmentMethodOfPayment: Optional[X12ID] = element(
        name="G6601",
        description="Shipment Method of Payment",
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="G6602",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    PalletExchangeCode: Optional[X12ID] = element(
        name="G6603",
        description="Pallet Exchange Code",
        min_length=1,
        max_length=1,
    )

    UnitLoadOptionCode: Optional[X12ID] = element(
        name="G6604",
        description="Unit Load Option Code",
        min_length=2,
        max_length=2,
    )

    Routing: Optional[X12AN] = element(
        name="G6605",
        description="Routing",
        min_length=1,
        max_length=35,
    )

    FOBPointCode: Optional[X12ID] = element(
        name="G6606",
        description="F.O.B. Point Code",
        min_length=2,
        max_length=2,
    )

    FOBPoint: Optional[X12AN] = element(
        name="G6607",
        description="F.O.B. Point",
        min_length=1,
        max_length=30,
    )
