# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TF(Segment):
    """
    TF - Tariff Information
    
    Description:
        To identify agency tariff
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TF/
    """
    _id: Literal["TF"] = id_element(name="TF")

    TariffAgencyCode: X12ID = element(
        name="TF01",
        description="Tariff Agency Code",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    TariffNumber: X12AN = element(
        name="TF02",
        description="Tariff Number",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    TariffNumberSuffix: Optional[X12AN] = element(
        name="TF03",
        description="Tariff Number Suffix",
        min_length=1,
        max_length=2,
    )

    TariffSupplementIdentifier: Optional[X12AN] = element(
        name="TF04",
        description="Tariff Supplement Identifier",
        min_length=1,
        max_length=4,
    )
