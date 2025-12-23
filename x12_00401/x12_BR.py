# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BR(Segment):
    """
    BR - Beginning Segment for Material Management
    
    Description:
        To indicate the beginning of a material management transaction and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BR/
    """
    _id: Literal["BR"] = id_element(name="BR")

    TransactionSetPurposeCode: X12ID = element(
        name="BR01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: X12ID = element(
        name="BR02",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BR03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="BR04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="BR05",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BR06",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="BR07",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BR08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Time: Optional[X12TM] = element(
        name="BR09",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="BR10",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BR11",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
