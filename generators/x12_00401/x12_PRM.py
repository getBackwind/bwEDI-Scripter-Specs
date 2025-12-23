# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PRM(Segment):
    """
    PRM - Basic Trace Parameters
    
    Description:
        To provide basic trace parameters
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PRM/
    """
    _id: Literal["PRM"] = id_element(name="PRM")

    CarTypeCode: Optional[X12ID] = element(
        name="PRM01",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    LoadEmptyStatusCode: Optional[X12ID] = element(
        name="PRM02",
        description="Load/Empty Status Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="PRM03",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="PRM04",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="PRM05",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    CommodityCode: Optional[X12AN] = element(
        name="PRM06",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="PRM07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="PRM08",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardPointLocationCode3: Optional[X12ID] = element(
        name="PRM09",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    StandardCarrierAlphaCode4: Optional[X12ID] = element(
        name="PRM10",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    TransportationConditionCode: Optional[X12ID] = element(
        name="PRM11",
        description="Transportation Condition Code",
        min_length=1,
        max_length=1,
    )

    AssociationOfAmericanRailroadsCarGradeCode: Optional[X12ID] = element(
        name="PRM12",
        description="Association of American Railroads Car Grade Code",
        min_length=1,
        max_length=1,
    )

    IntermodalServiceCode: Optional[X12ID] = element(
        name="PRM13",
        description="Intermodal Service Code",
        min_length=1,
        max_length=2,
    )
