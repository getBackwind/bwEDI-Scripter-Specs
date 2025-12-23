# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BCP(Segment):
    """
    BCP - Beginning Segment for Contract Pricing Proposal
    
    Description:
        To indicate the beginning of a Contract Pricing Proposal Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BCP/
    """
    _id: Literal["BCP"] = id_element(name="BCP")

    TransactionSetPurposeCode: X12ID = element(
        name="BCP01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="BCP02",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="BCP03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: Optional[X12DT] = element(
        name="BCP04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ContractActionCode: Optional[X12ID] = element(
        name="BCP05",
        description="Contract Action Code",
        min_length=2,
        max_length=2,
    )

    ContractTypeCode: Optional[X12ID] = element(
        name="BCP06",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )

    Date2: Optional[X12DT] = element(
        name="BCP07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BCP08",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ChangeOrderSequenceNumber: Optional[X12AN] = element(
        name="BCP09",
        description="Change Order Sequence Number",
        min_length=1,
        max_length=8,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BCP10",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="BCP11",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="BCP12",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description2: Optional[X12AN] = element(
        name="BCP13",
        description="Description",
        min_length=1,
        max_length=80,
    )
