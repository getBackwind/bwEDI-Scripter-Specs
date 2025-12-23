# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class BEN(Segment):
    """
    BEN - Beneficiary or Owner Information
    
    Description:
        To supply beneficiary, co-participant, and owner information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BEN/
    """
    _id: Literal["BEN"] = id_element(name="BEN")

    PrimaryOrContingentCode: Optional[X12ID] = element(
        name="BEN01",
        description="Primary or Contingent Code",
        min_length=1,
        max_length=1,
    )

    Percent: Optional[X12R] = element(
        name="BEN02",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    IndividualRelationshipCode: Optional[X12ID] = element(
        name="BEN03",
        description="Individual Relationship Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="BEN04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="BEN05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    TypeOfAccountCode: Optional[X12ID] = element(
        name="BEN06",
        description="Type of Account Code",
        min_length=2,
        max_length=2,
    )
