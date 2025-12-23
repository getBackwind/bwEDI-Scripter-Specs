# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12TM


class OTI(Segment):
    """
    OTI - Original Transaction Identification
    
    Description:
        To identify the edited transaction set and the level at which the results of the edit are reported, and to indicate the accepted, rejected, or accepted-with-change edit result
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/OTI/
    """
    _id: Literal["OTI"] = id_element(name="OTI")

    AcknowledgmentCode: X12ID = element(
        name="OTI01",
        description="Application Acknowledgment Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdQualifier: X12ID = element(
        name="OTI02",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceID: X12AN = element(
        name="OTI03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ApplicationSenderSCode: Optional[X12AN] = element(
        name="OTI04",
        description="Application Sender's Code",
        min_length=2,
        max_length=15,
    )

    ApplicationReceiverSCode: Optional[X12AN] = element(
        name="OTI05",
        description="Application Receiver's Code",
        min_length=2,
        max_length=15,
    )

    Date: Optional[X12DT] = element(
        name="OTI06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="OTI07",
        description="Time",
        min_length=4,
        max_length=8,
    )

    GroupControlNumber: Optional[X12Nn] = element(
        name="OTI08",
        description="Group Control Number",
        min_length=1,
        max_length=9,
    )

    TransactionSetControlNumber: Optional[X12AN] = element(
        name="OTI09",
        description="Transaction Set Control Number",
        min_length=4,
        max_length=9,
    )

    TransactionSetID: Optional[X12ID] = element(
        name="OTI10",
        description="Transaction Set Identifier Code",
        min_length=3,
        max_length=3,
    )

    VersionReleaseIndustryIdentifierCode: Optional[X12AN] = element(
        name="OTI11",
        description="Version / Release / Industry Identifier Code",
        min_length=1,
        max_length=12,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="OTI12",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="OTI13",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ApplicationType: Optional[X12ID] = element(
        name="OTI14",
        description="Application Type",
    )

    ActionCode: Optional[X12ID] = element(
        name="OTI15",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    TransactionHandlingCode: Optional[X12ID] = element(
        name="OTI16",
        description="Transaction Handling Code",
        min_length=1,
        max_length=1,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="OTI17",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )
