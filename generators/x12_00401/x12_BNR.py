# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BNR(Segment):
    """
    BNR - Beginning Segment For Nonconformance Report
    
    Description:
        To indicate the beginning of a Nonconformance Report Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BNR/
    """
    _id: Literal["BNR"] = id_element(name="BNR")

    TransactionSetPurposeCode: X12ID = element(
        name="BNR01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="BNR02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BNR03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BNR04",
        description="Time",
        min_length=4,
        max_length=8,
    )

    NonconformanceReportStatusCode: Optional[X12ID] = element(
        name="BNR05",
        description="Nonconformance Report Status Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BNR06",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
