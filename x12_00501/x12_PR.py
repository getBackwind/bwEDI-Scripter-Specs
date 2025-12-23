# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PR(Segment):
    """
    PR - Product (Commodity)
    
    Description:
        To identify the commodity to which the application of a rate docket is restricted
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PR/
    """
    _id: Literal["PR"] = id_element(name="PR")

    CommodityGeographicLogicalConnectorCode: X12ID = element(
        name="PR01",
        description="Commodity/Geographic Logical Connector Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CommodityCodeQualifier: Optional[X12ID] = element(
        name="PR02",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="PR03",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    CommodityCode2: Optional[X12AN] = element(
        name="PR04",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    ChangeTypeCode: Optional[X12ID] = element(
        name="PR05",
        description="Change Type Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="PR06",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    DocketControlNumber: Optional[X12AN] = element(
        name="PR07",
        description="Docket Control Number",
        min_length=1,
        max_length=7,
    )

    DocketIdentification: Optional[X12AN] = element(
        name="PR08",
        description="Docket Identification",
        min_length=1,
        max_length=11,
    )

    GroupTitle: Optional[X12AN] = element(
        name="PR09",
        description="Group Title",
        min_length=2,
        max_length=30,
    )
