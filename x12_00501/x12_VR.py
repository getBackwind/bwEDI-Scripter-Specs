# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class VR(Segment):
    """
    VR - Rate Origin
    
    Description:
        To provide rate-origin information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/VR/
    """
    _id: Literal["VR"] = id_element(name="VR")

    TransactionSetPurposeCode: X12ID = element(
        name="VR01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TariffNumber: X12AN = element(
        name="VR02",
        description="Tariff Number",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="VR03",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="VR04",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="VR05",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    CurrencyCode: X12ID = element(
        name="VR06",
        description="Currency Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    TariffAgencyCode: Optional[X12ID] = element(
        name="VR07",
        description="Tariff Agency Code",
        min_length=1,
        max_length=4,
    )

    TariffSupplementIdentifier: Optional[X12AN] = element(
        name="VR08",
        description="Tariff Supplement Identifier",
        min_length=1,
        max_length=4,
    )

    ExParte: Optional[X12AN] = element(
        name="VR09",
        description="Ex Parte",
        min_length=4,
        max_length=4,
    )
