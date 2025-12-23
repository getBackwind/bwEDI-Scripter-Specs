# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BTP(Segment):
    """
    BTP - Beginning Segment For Trading Partner Profile
    
    Description:
        To indicate the type and purpose of the profile data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BTP/
    """
    _id: Literal["BTP"] = id_element(name="BTP")

    TransactionSetPurposeCode: X12ID = element(
        name="BTP01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="BTP02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BTP03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: X12TM = element(
        name="BTP04",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    TransactionTypeCode: X12ID = element(
        name="BTP05",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TransactionSetPurposeCode2: Optional[X12ID] = element(
        name="BTP06",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BTP07",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date2: Optional[X12DT] = element(
        name="BTP08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="BTP09",
        description="Time",
        min_length=4,
        max_length=8,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="BTP10",
        description="Payment Method Code",
        min_length=3,
        max_length=3,
    )
