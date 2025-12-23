# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class IMA(Segment):
    """
    IMA - Interchange Move Authority
    
    Description:
        To identify the transportation interchange authority
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IMA/
    """
    _id: Literal["IMA"] = id_element(name="IMA")

    MovementAuthorityCode: X12ID = element(
        name="IMA01",
        description="Movement Authority Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="IMA02",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    TariffApplicationCode: Optional[X12ID] = element(
        name="IMA03",
        description="Tariff Application Code",
        min_length=1,
        max_length=1,
    )

    TariffApplicationCode2: Optional[X12ID] = element(
        name="IMA04",
        description="Tariff Application Code",
        min_length=1,
        max_length=1,
    )
