# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class W66(Segment):
    """
    W66 - Warehouse Carrier Information
    
    Description:
        To specify transportation instructions relating to shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W66/
    """
    _id: Literal["W66"] = id_element(name="W66")

    ShipmentMethodOfPayment: X12ID = element(
        name="W6601",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    TransportationMethodTypeCode: X12ID = element(
        name="W6602",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    PalletExchangeCode: Optional[X12ID] = element(
        name="W6603",
        description="Pallet Exchange Code",
        min_length=1,
        max_length=1,
    )

    UnitLoadOptionCode: Optional[X12ID] = element(
        name="W6604",
        description="Unit Load Option Code",
        min_length=2,
        max_length=2,
    )

    Routing: Optional[X12AN] = element(
        name="W6605",
        description="Routing",
        min_length=1,
        max_length=35,
    )

    FOBPointCode: Optional[X12ID] = element(
        name="W6606",
        description="F.O.B. Point Code",
        min_length=2,
        max_length=2,
    )

    FOBPoint: Optional[X12AN] = element(
        name="W6607",
        description="F.O.B. Point",
        min_length=1,
        max_length=30,
    )

    CODMethodOfPaymentCode: Optional[X12ID] = element(
        name="W6608",
        description="COD Method of Payment Code",
        min_length=1,
        max_length=1,
    )

    Amount: Optional[X12Nn] = element(
        name="W6609",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="W6610",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
