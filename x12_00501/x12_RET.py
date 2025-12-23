# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class RET(Segment):
    """
    RET - Real Estate Transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RET/
    """
    _id: Literal["RET"] = id_element(name="RET")

    InformationStatusCode: Optional[X12ID] = element(
        name="RET01",
        description="Information Status Code",
        min_length=1,
        max_length=1,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="RET02",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    StatusCode: Optional[X12ID] = element(
        name="RET03",
        description="Status Code",
        min_length=2,
        max_length=2,
    )

    StatusOfPlansForRealEstateAssetCode: Optional[X12ID] = element(
        name="RET04",
        description="Status of Plans for Real Estate Asset Code",
        min_length=1,
        max_length=1,
    )

    ContractTypeCode: Optional[X12ID] = element(
        name="RET05",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )
