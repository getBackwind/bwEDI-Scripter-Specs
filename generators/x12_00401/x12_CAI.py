# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CAI(Segment):
    """
    CAI - Civil Action Income
    
    Description:
        To name the income pursuant to a civil action (judgment, child support, etc.)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CAI/
    """
    _id: Literal["CAI"] = id_element(name="CAI")

    PublicRecordOrObligationCode: X12ID = element(
        name="CAI01",
        description="Public Record or Obligation Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Name: X12AN = element(
        name="CAI02",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    Name2: Optional[X12AN] = element(
        name="CAI03",
        description="Name",
        min_length=1,
        max_length=60,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="CAI04",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="CAI05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="CAI06",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CAI07",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
