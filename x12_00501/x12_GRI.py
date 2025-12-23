# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class GRI(Segment):
    """
    GRI - Statistical Government Information
    
    Description:
        To respond to a specific government reporting requirement
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/GRI/
    """
    _id: Literal["GRI"] = id_element(name="GRI")

    ReportedDataIDCode: X12AN = element(
        name="GRI01",
        description="Reported Data ID Code",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    ReportedDataResponse: Optional[X12AN] = element(
        name="GRI02",
        description="Reported Data Response",
        min_length=1,
        max_length=10,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="GRI03",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="GRI04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="GRI05",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="GRI06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentQualifier: Optional[X12ID] = element(
        name="GRI07",
        description="Percent Qualifier",
        min_length=1,
        max_length=2,
    )

    PercentIntegerFormat: Optional[X12Nn] = element(
        name="GRI08",
        description="Percent, Integer Format",
        min_length=1,
        max_length=3,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="GRI09",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="GRI10",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Description: Optional[X12AN] = element(
        name="GRI11",
        description="Description",
        min_length=1,
        max_length=80,
    )
