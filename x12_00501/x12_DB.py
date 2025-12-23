# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DB(Segment):
    """
    DB - Disbursement Information
    
    Description:
        To specify disbursement dates and amounts for a loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DB/
    """
    _id: Literal["DB"] = id_element(name="DB")

    DateTimePeriodFormatQualifier: X12ID = element(
        name="DB01",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="DB02",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    MonetaryAmount: X12R = element(
        name="DB03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="DB04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="DB05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="DB06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
