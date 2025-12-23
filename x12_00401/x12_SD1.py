# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SD1(Segment):
    """
    SD1 - Safety Data
    
    Description:
        To provide safety data information to recipients of the transaction, including identification of the hazard that the material being described represents, and the organization or party which declared this material to be a hazard or established exposure limits or other guidelines for that material
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SD1/
    """
    _id: Literal["SD1"] = id_element(name="SD1")

    ItemDescriptionType: X12ID = element(
        name="SD101",
        description="Item Description Type",
        mandatory=True,
    )

    SafetyCharacteristicHazardCode: X12ID = element(
        name="SD102",
        description="Safety Characteristic/Hazard Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="SD103",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="SD104",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    ProductDescriptionCode: Optional[X12AN] = element(
        name="SD105",
        description="Product Description Code",
        min_length=1,
        max_length=12,
    )

    Description: Optional[X12AN] = element(
        name="SD106",
        description="Description",
        min_length=1,
        max_length=80,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="SD107",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="SD108",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
