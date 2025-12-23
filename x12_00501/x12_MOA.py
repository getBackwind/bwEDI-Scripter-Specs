# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12R


class MOA(Segment):
    """
    MOA - Medicare Outpatient Adjudication
    
    Description:
        To convey claim-level data related to the adjudication of Medicare claims not related to an inpatient setting
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MOA/
    """
    _id: Literal["MOA"] = id_element(name="MOA")

    PercentageAsDecimal: Optional[X12R] = element(
        name="MOA01",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="MOA02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="MOA03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="MOA04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="MOA05",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification4: Optional[X12AN] = element(
        name="MOA06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification5: Optional[X12AN] = element(
        name="MOA07",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="MOA08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="MOA09",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
