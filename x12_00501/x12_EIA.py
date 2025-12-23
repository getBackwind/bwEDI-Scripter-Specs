# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class EIA(Segment):
    """
    EIA - Beginning Segment for Equipment Inquiry or Advice
    
    Description:
        To identify functions and provide control information required for the Equipment Inquiry or Advice Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EIA/
    """
    _id: Literal["EIA"] = id_element(name="EIA")

    TransactionSetPurposeCode: X12ID = element(
        name="EIA01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="EIA02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="EIA03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="EIA04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Count: Optional[X12Nn] = element(
        name="EIA05",
        description="Count",
        min_length=1,
        max_length=9,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="EIA06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
