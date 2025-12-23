# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BTR(Segment):
    """
    BTR - Beginning Segment for Test Results
    
    Description:
        To indicate the beginning of a test results transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BTR/
    """
    _id: Literal["BTR"] = id_element(name="BTR")

    TransactionSetPurposeCode: X12ID = element(
        name="BTR01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BTR02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BTR03",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReportTypeCode: Optional[X12ID] = element(
        name="BTR04",
        description="Report Type Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BTR05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BTR06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BTR07",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )
