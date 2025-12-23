# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PM(Segment):
    """
    PM - Electronic Funds Transfer Information
    
    Description:
        To supply information on the electronic funds transfer (EFT) method of payment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PM/
    """
    _id: Literal["PM"] = id_element(name="PM")

    DFIIdentificationNumber: X12AN = element(
        name="PM01",
        description="(DFI) Identification Number",
        mandatory=True,
        min_length=3,
        max_length=12,
    )

    AccountNumber: X12AN = element(
        name="PM02",
        description="Account Number",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="PM03",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: X12ID = element(
        name="PM04",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AccountNumberQualifier: Optional[X12ID] = element(
        name="PM05",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    DFIIDNumberQualifier: Optional[X12ID] = element(
        name="PM06",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )
