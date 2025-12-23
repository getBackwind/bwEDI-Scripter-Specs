# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class GY(Segment):
    """
    GY - Geography
    
    Description:
        To define the geographic region from or to which a rate docket applies
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/GY/
    """
    _id: Literal["GY"] = id_element(name="GY")

    GeographyQualifierCode: X12ID = element(
        name="GY01",
        description="Geography Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CommodityGeographicLogicalConnectorCode: Optional[X12ID] = element(
        name="GY02",
        description="Commodity/Geographic Logical Connector Code",
        min_length=1,
        max_length=1,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="GY03",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="GY04",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="GY05",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="GY06",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="GY07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ChangeTypeCode: Optional[X12ID] = element(
        name="GY08",
        description="Change Type Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="GY09",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    DocketControlNumber: Optional[X12AN] = element(
        name="GY10",
        description="Docket Control Number",
        min_length=1,
        max_length=7,
    )

    DocketIdentification: Optional[X12AN] = element(
        name="GY11",
        description="Docket Identification",
        min_length=1,
        max_length=11,
    )

    GroupTitle: Optional[X12AN] = element(
        name="GY12",
        description="Group Title",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="GY13",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="GY14",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="GY15",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
