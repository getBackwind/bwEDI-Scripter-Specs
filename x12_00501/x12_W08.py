# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class W08(Segment):
    """
    W08 - Receipt Carrier Information
    
    Description:
        To identify carrier equipment and condition
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W08/
    """
    _id: Literal["W08"] = id_element(name="W08")

    TransportationMethodTypeCode: X12ID = element(
        name="W0801",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="W0802",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Routing: Optional[X12AN] = element(
        name="W0803",
        description="Routing",
        min_length=1,
        max_length=35,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="W0804",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="W0805",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    SealNumber: Optional[X12AN] = element(
        name="W0806",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    SealNumber2: Optional[X12AN] = element(
        name="W0807",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    SealStatusCode: Optional[X12ID] = element(
        name="W0808",
        description="Seal Status Code",
        min_length=2,
        max_length=2,
    )

    UnitLoadOptionCode: Optional[X12ID] = element(
        name="W0809",
        description="Unit Load Option Code",
        min_length=2,
        max_length=2,
    )
