# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R, X12TM


class CUR(Segment):
    """
    CUR - Currency
    
    Description:
        To specify the currency (dollars, pounds, francs, etc.) used in a transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CUR/
    """
    _id: Literal["CUR"] = id_element(name="CUR")

    EntityIdentifierCode: X12ID = element(
        name="CUR01",
        description="Entity Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    CurrencyCode: X12ID = element(
        name="CUR02",
        description="Currency Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    ExchangeRate: Optional[X12R] = element(
        name="CUR03",
        description="Exchange Rate",
        min_length=4,
        max_length=10,
    )

    EntityIdentifierCode2: Optional[X12ID] = element(
        name="CUR04",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    CurrencyCode2: Optional[X12ID] = element(
        name="CUR05",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    CurrencyMarketExchangeCode: Optional[X12ID] = element(
        name="CUR06",
        description="Currency Market/Exchange Code",
        min_length=3,
        max_length=3,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="CUR07",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="CUR08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="CUR09",
        description="Time",
        min_length=4,
        max_length=8,
    )

    DateTimeQualifier2: Optional[X12ID] = element(
        name="CUR10",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="CUR11",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="CUR12",
        description="Time",
        min_length=4,
        max_length=8,
    )

    DateTimeQualifier3: Optional[X12ID] = element(
        name="CUR13",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date3: Optional[X12DT] = element(
        name="CUR14",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time3: Optional[X12TM] = element(
        name="CUR15",
        description="Time",
        min_length=4,
        max_length=8,
    )

    DateTimeQualifier4: Optional[X12ID] = element(
        name="CUR16",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date4: Optional[X12DT] = element(
        name="CUR17",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time4: Optional[X12TM] = element(
        name="CUR18",
        description="Time",
        min_length=4,
        max_length=8,
    )

    DateTimeQualifier5: Optional[X12ID] = element(
        name="CUR19",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date5: Optional[X12DT] = element(
        name="CUR20",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time5: Optional[X12TM] = element(
        name="CUR21",
        description="Time",
        min_length=4,
        max_length=8,
    )
