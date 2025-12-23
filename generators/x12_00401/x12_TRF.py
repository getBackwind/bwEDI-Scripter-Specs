# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class TRF(Segment):
    """
    TRF - Rating Factors
    
    Description:
        To specify rating information used to calculate usage-sensitive charges
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TRF/
    """
    _id: Literal["TRF"] = id_element(name="TRF")

    QuantityQualifier: X12ID = element(
        name="TRF01",
        description="Quantity Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: X12R = element(
        name="TRF03",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Quantity2: X12R = element(
        name="TRF05",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )
