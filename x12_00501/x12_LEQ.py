# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class LEQ(Segment):
    """
    LEQ - Leased Equipment Information
    
    Description:
        To communicate necessary data for car hire settlements with leased equipment and identify billing parties and allowed dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LEQ/
    """
    _id: Literal["LEQ"] = id_element(name="LEQ")

    ReferenceIdentificationQualifier: X12ID = element(
        name="LEQ01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="LEQ02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Year: X12Nn = element(
        name="LEQ03",
        description="Year",
        mandatory=True,
        min_length=4,
        max_length=4,
    )

    MonthOfTheYearCode: X12ID = element(
        name="LEQ04",
        description="Month of the Year Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="LEQ05",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    ReferenceIdentification2: X12AN = element(
        name="LEQ06",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    MonetaryAmount: X12R = element(
        name="LEQ07",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Date: Optional[X12DT] = element(
        name="LEQ08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ExchangeRate: Optional[X12R] = element(
        name="LEQ09",
        description="Exchange Rate",
        min_length=4,
        max_length=10,
    )
