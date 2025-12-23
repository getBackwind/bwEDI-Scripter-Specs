# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class JCT(Segment):
    """
    JCT - Railroad Junction Information
    
    Description:
        To indicate railroad junction carriers and interchange information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/JCT/
    """
    _id: Literal["JCT"] = id_element(name="JCT")

    StandardCarrierAlphaCode: X12ID = element(
        name="JCT01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: X12ID = element(
        name="JCT02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    FreightStationAccountingCode: X12ID = element(
        name="JCT03",
        description="Freight Station Accounting Code",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    FreightStationAccountingCode2: X12ID = element(
        name="JCT04",
        description="Freight Station Accounting Code",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    StandardCarrierAlphaCode3: X12ID = element(
        name="JCT05",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode4: X12ID = element(
        name="JCT06",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="JCT07",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    InterchangeTypeCode: X12ID = element(
        name="JCT08",
        description="Interchange Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: X12ID = element(
        name="JCT09",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
