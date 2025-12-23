# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class FTH(Segment):
    """
    FTH - First Time Home Buyer
    
    Description:
        To capture the first time home buyer information found in section of the Loan Application
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FTH/
    """
    _id: Literal["FTH"] = id_element(name="FTH")

    YesNoConditionOrResponseCode: X12ID = element(
        name="FTH01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="FTH02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    TypeOfResidenceCode: Optional[X12ID] = element(
        name="FTH03",
        description="Type of Residence Code",
        min_length=1,
        max_length=1,
    )

    TypeOfAccountCode: Optional[X12ID] = element(
        name="FTH04",
        description="Type of Account Code",
        min_length=2,
        max_length=2,
    )
