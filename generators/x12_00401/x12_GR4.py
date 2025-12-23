# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class GR4(Segment):
    """
    GR4 - Loading Cluster
    
    Description:
        To define loading configuration type of the units being loaded
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/GR4/
    """
    _id: Literal["GR4"] = id_element(name="GR4")

    ConfigurationTypeCode: X12ID = element(
        name="GR401",
        description="Configuration Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    EquipmentDescriptionCode: X12ID = element(
        name="GR402",
        description="Equipment Description Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    EquipmentUseCode: X12ID = element(
        name="GR403",
        description="Equipment Use Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="GR404",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="GR405",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="GR406",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="GR407",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="GR408",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    CityName: Optional[X12AN] = element(
        name="GR409",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="GR410",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="GR411",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
