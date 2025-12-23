# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class DEP(Segment):
    """
    DEP - Deposit
    
    Description:
        To indicate the lockbox ID, date, time, deposit number, and bank account information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DEP/
    """
    _id: Literal["DEP"] = id_element(name="DEP")

    ReferenceIdentification: X12AN = element(
        name="DEP01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: X12DT = element(
        name="DEP02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="DEP03",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="DEP04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    DFIIDNumberQualifier: X12ID = element(
        name="DEP05",
        description="(DFI) ID Number Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber: X12AN = element(
        name="DEP06",
        description="(DFI) Identification Number",
        mandatory=True,
        min_length=3,
        max_length=12,
    )

    AccountNumberQualifier: Optional[X12ID] = element(
        name="DEP07",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    AccountNumber: Optional[X12AN] = element(
        name="DEP08",
        description="Account Number",
        min_length=1,
        max_length=35,
    )
