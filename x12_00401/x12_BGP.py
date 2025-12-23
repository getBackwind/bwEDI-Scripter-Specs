# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BGP(Segment):
    """
    BGP - Beginning Segment for Problem Log Inquiry or Advice
    
    Description:
        To provide identifying numbers associated with the creation and maintenance of Interline Service Management problem logs
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BGP/
    """
    _id: Literal["BGP"] = id_element(name="BGP")

    TransactionSetPurposeCode: X12ID = element(
        name="BGP01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProblemLogReasonCode: Optional[X12ID] = element(
        name="BGP02",
        description="Problem Log Reason Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="BGP03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BGP04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="BGP05",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="BGP06",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="BGP07",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="BGP08",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    InterchangeTrainIdentification: Optional[X12AN] = element(
        name="BGP09",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )
