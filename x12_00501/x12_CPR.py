# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R


class CPR(Segment):
    """
    CPR - Commodity Price Reference
    
    Description:
        To provide a specific price on a specified date for a given commodity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CPR/
    """
    _id: Literal["CPR"] = id_element(name="CPR")

    MarketExchangeIdentifier: X12ID = element(
        name="CPR01",
        description="Market Exchange Identifier",
        mandatory=True,
    )

    Date: X12DT = element(
        name="CPR02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    UnitPrice: X12R = element(
        name="CPR03",
        description="Unit Price",
        mandatory=True,
        min_length=1,
        max_length=17,
    )

    CommodityIdentification: X12ID = element(
        name="CPR04",
        description="Commodity Identification",
        mandatory=True,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CPR05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
