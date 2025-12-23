# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12R


class PLB(Segment):
    """
    PLB - Provider Level Adjustment
    
    Description:
        To convey provider level adjustment information for debit or credit transactions such as, accelerated payments, cost report settlements for a fiscal year and timeliness report penalties unrelated to a specific claim or service
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PLB/
    """
    _id: Literal["PLB"] = id_element(name="PLB")

    ReferenceIdentification: X12AN = element(
        name="PLB01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: X12DT = element(
        name="PLB02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    MonetaryAmount: X12R = element(
        name="PLB04",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="PLB06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="PLB08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="PLB10",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="PLB12",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount6: Optional[X12R] = element(
        name="PLB14",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
