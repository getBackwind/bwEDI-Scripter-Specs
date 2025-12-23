# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class CTB(Segment):
    """
    CTB - Restrictions/Conditions
    
    Description:
        To specify restrictions/conditions (such as shipping, ordering)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CTB/
    """
    _id: Literal["CTB"] = id_element(name="CTB")

    RestrictionsQualifier: X12ID = element(
        name="CTB01",
        description="Restrictions/Conditions Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="CTB02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="CTB03",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="CTB04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="CTB05",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    Amount: Optional[X12Nn] = element(
        name="CTB06",
        description="Amount",
        min_length=1,
        max_length=15,
    )
