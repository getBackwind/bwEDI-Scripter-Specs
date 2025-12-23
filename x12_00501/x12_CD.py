# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class CD(Segment):
    """
    CD - Shipment Conditions
    
    Description:
        To specify condition restrictions or provisions applicable to the rate docket
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CD/
    """
    _id: Literal["CD"] = id_element(name="CD")

    ConditionSegmentLogicalConnector: X12AN = element(
        name="CD01",
        description="Condition Segment Logical Connector",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    ConditionCode: Optional[X12ID] = element(
        name="CD02",
        description="Condition Code",
        min_length=4,
        max_length=4,
    )

    ConditionValue: Optional[X12AN] = element(
        name="CD03",
        description="Condition Value",
        min_length=1,
        max_length=10,
    )

    ConditionValue2: Optional[X12AN] = element(
        name="CD04",
        description="Condition Value",
        min_length=1,
        max_length=10,
    )

    ConditionValue3: Optional[X12AN] = element(
        name="CD05",
        description="Condition Value",
        min_length=1,
        max_length=10,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="CD06",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )

    ChangeTypeCode: Optional[X12ID] = element(
        name="CD07",
        description="Change Type Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="CD08",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    DocketControlNumber: Optional[X12AN] = element(
        name="CD09",
        description="Docket Control Number",
        min_length=1,
        max_length=7,
    )

    DocketIdentification: Optional[X12AN] = element(
        name="CD10",
        description="Docket Identification",
        min_length=1,
        max_length=11,
    )

    GroupTitle: Optional[X12AN] = element(
        name="CD11",
        description="Group Title",
        min_length=2,
        max_length=30,
    )
