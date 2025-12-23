# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class DED(Segment):
    """
    DED - Deductions
    
    Description:
        To specify payment related information for child support payment deductions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DED/
    """
    _id: Literal["DED"] = id_element(name="DED")

    TypeOfDeduction: X12ID = element(
        name="DED01",
        description="Type of Deduction",
        mandatory=True,
    )

    ReferenceIdentification: X12AN = element(
        name="DED02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="DED03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Amount: X12Nn = element(
        name="DED04",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    ReferenceIdentification2: X12AN = element(
        name="DED05",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="DED06",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Name: Optional[X12AN] = element(
        name="DED07",
        description="Name",
        min_length=1,
        max_length=60,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="DED08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="DED09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
