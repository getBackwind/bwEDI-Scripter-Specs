# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class ASL(Segment):
    """
    ASL - Asset Liability
    
    Description:
        To report financial information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ASL/
    """
    _id: Literal["ASL"] = id_element(name="ASL")

    AmountQualifierCode: X12ID = element(
        name="ASL01",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="ASL02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    AssetLiabilityTypeCode: Optional[X12ID] = element(
        name="ASL03",
        description="Asset Liability Type Code",
        min_length=2,
        max_length=2,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="ASL04",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )
