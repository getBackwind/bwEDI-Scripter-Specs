# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class BPT(Segment):
    """
    BPT - Beginning Segment for Product Transfer and Resale
    
    Description:
        To indicate the beginning of the Product Transfer and Resale Report Transaction Set and transmit identifying data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BPT/
    """
    _id: Literal["BPT"] = id_element(name="BPT")

    TransactionSetPurposeCode: X12ID = element(
        name="BPT01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BPT02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BPT03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReportTypeCode: Optional[X12ID] = element(
        name="BPT04",
        description="Report Type Code",
        min_length=2,
        max_length=2,
    )

    PriceMultiplierQualifier: Optional[X12ID] = element(
        name="BPT05",
        description="Price Multiplier Qualifier",
        min_length=3,
        max_length=3,
    )

    Multiplier: Optional[X12R] = element(
        name="BPT06",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    ActionCode: Optional[X12ID] = element(
        name="BPT07",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="BPT08",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BPT09",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BPT10",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )
