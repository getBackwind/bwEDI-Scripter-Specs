# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class CI(Segment):
    """
    CI - Carrier Interchange Agreement
    
    Description:
        To identify motor carriers and the status of their interchange agreements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CI/
    """
    _id: Literal["CI"] = id_element(name="CI")

    Name: Optional[X12AN] = element(
        name="CI01",
        description="Name",
        min_length=1,
        max_length=60,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="CI02",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="CI03",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="CI04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="CI05",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="CI06",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    InterchangeAgreementStatusCode: Optional[X12ID] = element(
        name="CI07",
        description="Interchange Agreement Status Code",
        min_length=1,
        max_length=1,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="CI08",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="CI09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    DateTimeQualifier2: Optional[X12ID] = element(
        name="CI10",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="CI11",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Name2: Optional[X12AN] = element(
        name="CI12",
        description="Name",
        min_length=1,
        max_length=60,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="CI13",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CI14",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
