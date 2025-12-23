# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BOS(Segment):
    """
    BOS - Beginning Segment for Joint Interest Billing and Operating Expense Statement
    
    Description:
        To indicate the beginning of a joint interest billing and operating expense statement transaction and to transmit the identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BOS/
    """
    _id: Literal["BOS"] = id_element(name="BOS")

    StatementNumber: X12AN = element(
        name="BOS01",
        description="Statement Number",
        mandatory=True,
        min_length=1,
        max_length=16,
    )

    Date: X12DT = element(
        name="BOS02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="BOS03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    StatementFormatCode: Optional[X12ID] = element(
        name="BOS04",
        description="Statement Format Code",
        min_length=6,
        max_length=6,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BOS05",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    Date2: Optional[X12DT] = element(
        name="BOS06",
        description="Date",
        min_length=8,
        max_length=8,
    )
