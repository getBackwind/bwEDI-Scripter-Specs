# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BCO(Segment):
    """
    BCO - Beginning Segment for Procurement Notices
    
    Description:
        To indicate the beginning of the Procurement Notices Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BCO/
    """
    _id: Literal["BCO"] = id_element(name="BCO")

    TransactionSetPurposeCode: X12ID = element(
        name="BCO01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RequestForQuoteReferenceNumber: Optional[X12AN] = element(
        name="BCO02",
        description="Request for Quote Reference Number",
        min_length=1,
        max_length=45,
    )

    Date: Optional[X12DT] = element(
        name="BCO03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BCO04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ContractStatusCode: Optional[X12ID] = element(
        name="BCO05",
        description="Contract Status Code",
        min_length=2,
        max_length=2,
    )

    Date2: Optional[X12DT] = element(
        name="BCO06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date3: Optional[X12DT] = element(
        name="BCO07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AcknowledgmentType: Optional[X12ID] = element(
        name="BCO08",
        description="Acknowledgment Type",
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="BCO09",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BCO10",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BCO11",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BCO12",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
