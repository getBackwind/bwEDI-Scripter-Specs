# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BTI(Segment):
    """
    BTI - Beginning Tax Information
    
    Description:
        To indicate the type of tax information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BTI/
    """
    _id: Literal["BTI"] = id_element(name="BTI")

    ReferenceIdentificationQualifier: X12ID = element(
        name="BTI01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="BTI02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="BTI03",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="BTI04",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    Date: Optional[X12DT] = element(
        name="BTI05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    NameControlIdentifier: Optional[X12AN] = element(
        name="BTI06",
        description="Name Control Identifier",
        min_length=1,
        max_length=4,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="BTI07",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="BTI08",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier3: Optional[X12ID] = element(
        name="BTI09",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode3: Optional[X12AN] = element(
        name="BTI10",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier4: Optional[X12ID] = element(
        name="BTI11",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode4: Optional[X12AN] = element(
        name="BTI12",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BTI13",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BTI14",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
