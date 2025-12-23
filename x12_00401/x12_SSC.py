# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class SSC(Segment):
    """
    SSC - Beginning Segment for Service Commitment Advice
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SSC/
    """
    _id: Literal["SSC"] = id_element(name="SSC")

    TransactionSetPurposeCode: X12ID = element(
        name="SSC01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="SSC02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="SSC03",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="SSC04",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    IdentificationCode: X12AN = element(
        name="SSC05",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    ServiceCommitmentTypeCode: X12ID = element(
        name="SSC06",
        description="Service Commitment Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    LoadEmptyStatusCode: X12ID = element(
        name="SSC07",
        description="Load/Empty Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Percent: Optional[X12Nn] = element(
        name="SSC08",
        description="Percent",
        min_length=1,
        max_length=3,
    )
