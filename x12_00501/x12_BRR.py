# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BRR(Segment):
    """
    BRR - Beginning Segment for Railroad Mark Register Update Activity
    
    Description:
        To indicate the nature of the activity being reported and identify the company involved
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BRR/
    """
    _id: Literal["BRR"] = id_element(name="BRR")

    TransactionSetPurposeCode: X12ID = element(
        name="BRR01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="BRR02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: X12ID = element(
        name="BRR03",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="BRR04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="BRR05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="BRR06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
