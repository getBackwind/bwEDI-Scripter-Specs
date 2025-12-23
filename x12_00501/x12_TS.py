# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TS(Segment):
    """
    TS - Tariff Section
    
    Description:
        To define the beginning of a section that contains specific tariff information; it will define tariff information that follows
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TS/
    """
    _id: Literal["TS"] = id_element(name="TS")

    TariffSectionIdentifier: Optional[X12AN] = element(
        name="TS01",
        description="Tariff Section Identifier",
        min_length=1,
        max_length=4,
    )

    TariffItemNumber: Optional[X12AN] = element(
        name="TS02",
        description="Tariff Item Number",
        min_length=1,
        max_length=16,
    )

    TariffItemSuffix: Optional[X12AN] = element(
        name="TS03",
        description="Tariff Item Suffix",
        min_length=1,
        max_length=4,
    )

    TariffSectionIDCode: Optional[X12ID] = element(
        name="TS04",
        description="Tariff Section ID Code",
        min_length=2,
        max_length=2,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="TS05",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="TS06",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="TS07",
        description="Description",
        min_length=1,
        max_length=80,
    )
