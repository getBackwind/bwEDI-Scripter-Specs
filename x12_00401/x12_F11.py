# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class F11(Segment):
    """
    F11 - Status
    
    Description:
        To identify a loss or damage claim and to indicate its status
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/F11/
    """
    _id: Literal["F11"] = id_element(name="F11")

    Date: X12DT = element(
        name="F1101",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification: X12AN = element(
        name="F1102",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="F1103",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Amount: Optional[X12Nn] = element(
        name="F1104",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount2: Optional[X12Nn] = element(
        name="F1105",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    StatusCode: X12ID = element(
        name="F1106",
        description="Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date2: X12DT = element(
        name="F1107",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    DeclineAmendReasonCode: Optional[X12ID] = element(
        name="F1108",
        description="Decline/Amend Reason Code",
        min_length=3,
        max_length=3,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="F1109",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="F1110",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )
