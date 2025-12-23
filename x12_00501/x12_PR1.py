# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PR1(Segment):
    """
    PR1 - Price Request Parameter List 1
    
    Description:
        To request price information based on certain parameters such as commodity, origin, and destination
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PR1/
    """
    _id: Literal["PR1"] = id_element(name="PR1")

    CommodityCodeQualifier: X12ID = element(
        name="PR101",
        description="Commodity Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CommodityCode: X12AN = element(
        name="PR102",
        description="Commodity Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    CommodityCode2: Optional[X12AN] = element(
        name="PR103",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="PR104",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="PR105",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="PR106",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="PR107",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="PR108",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    LocationQualifier2: Optional[X12ID] = element(
        name="PR109",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier3: Optional[X12AN] = element(
        name="PR110",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier4: Optional[X12AN] = element(
        name="PR111",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="PR112",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="PR113",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
