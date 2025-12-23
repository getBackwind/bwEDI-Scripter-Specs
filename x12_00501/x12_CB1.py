# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class CB1(Segment):
    """
    CB1 - Contract and Cost Accounting Standards Data
    
    Description:
        To specify contract and cost accounting standards data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CB1/
    """
    _id: Literal["CB1"] = id_element(name="CB1")

    AcquisitionDataCode: X12ID = element(
        name="CB101",
        description="Acquisition Data Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    FinancingTypeCode: Optional[X12ID] = element(
        name="CB102",
        description="Financing Type Code",
        min_length=1,
        max_length=1,
    )
