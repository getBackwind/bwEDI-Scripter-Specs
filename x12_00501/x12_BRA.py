# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BRA(Segment):
    """
    BRA - Beginning Segment for Receiving Advice or Acceptance Certificate
    
    Description:
        To indicate the beginning of a Receiving Advice or Acceptance Certificate Transaction Set and transmit an identifying number, date, and time
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BRA/
    """
    _id: Literal["BRA"] = id_element(name="BRA")

    ReferenceIdentification: X12AN = element(
        name="BRA01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: X12DT = element(
        name="BRA02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    TransactionSetPurposeCode: X12ID = element(
        name="BRA03",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReceivingAdviceOrAcceptanceCertificateTypeCode: X12ID = element(
        name="BRA04",
        description="Receiving Advice or Acceptance Certificate Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Time: Optional[X12TM] = element(
        name="BRA05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReceivingConditionCode: Optional[X12ID] = element(
        name="BRA06",
        description="Receiving Condition Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BRA07",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
