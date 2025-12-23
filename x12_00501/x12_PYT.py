# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class PYT(Segment):
    """
    PYT - Historical Payment Terms
    
    Description:
        To specify payment terms provided by a vendor to an entity over a historical period
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PYT/
    """
    _id: Literal["PYT"] = id_element(name="PYT")

    TermsNetDays: Optional[X12Nn] = element(
        name="PYT01",
        description="Terms Net Days",
        min_length=1,
        max_length=3,
    )

    TermsTypeCode: Optional[X12ID] = element(
        name="PYT02",
        description="Terms Type Code",
        min_length=2,
        max_length=2,
    )

    DayOfMonth: Optional[X12Nn] = element(
        name="PYT03",
        description="Day of Month",
        min_length=1,
        max_length=2,
    )

    TermsDiscountPercent: Optional[X12R] = element(
        name="PYT04",
        description="Terms Discount Percent",
        min_length=1,
        max_length=6,
    )

    TermsDiscountPercent2: Optional[X12R] = element(
        name="PYT05",
        description="Terms Discount Percent",
        min_length=1,
        max_length=6,
    )

    TermsTypeCode2: Optional[X12ID] = element(
        name="PYT06",
        description="Terms Type Code",
        min_length=2,
        max_length=2,
    )

    TermsDiscountDaysDue: Optional[X12Nn] = element(
        name="PYT07",
        description="Terms Discount Days Due",
        min_length=1,
        max_length=3,
    )

    TermsDiscountDaysDue2: Optional[X12Nn] = element(
        name="PYT08",
        description="Terms Discount Days Due",
        min_length=1,
        max_length=3,
    )
