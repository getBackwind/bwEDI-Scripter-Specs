# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PDP(Segment):
    """
    PDP - Property Description - Personal
    
    Description:
        To provide a description of personal property
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PDP/
    """
    _id: Literal["PDP"] = id_element(name="PDP")

    TypeOfPersonalOrBusinessAssetCode: X12ID = element(
        name="PDP01",
        description="Type of Personal or Business Asset Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CommodityCodeQualifier: Optional[X12ID] = element(
        name="PDP02",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="PDP03",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )
