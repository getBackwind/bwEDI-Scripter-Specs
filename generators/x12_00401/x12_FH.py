# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class FH(Segment):
    """
    FH - Family History
    
    Description:
        To report information about a person's family health history
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FH/
    """
    _id: Literal["FH"] = id_element(name="FH")

    IndividualRelationshipCode: X12ID = element(
        name="FH01",
        description="Individual Relationship Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="FH02",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="FH03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    CurrentHealthConditionCode: Optional[X12ID] = element(
        name="FH04",
        description="Current Health Condition Code",
        min_length=1,
        max_length=1,
    )
