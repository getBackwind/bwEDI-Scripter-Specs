# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12R


class MIA(Segment):
    """
    MIA - Medicare Inpatient Adjudication
    
    Description:
        To provide claim-level data related to the adjudication of Medicare inpatient claims
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MIA/
    """
    _id: Literal["MIA"] = id_element(name="MIA")

    Quantity: X12R = element(
        name="MIA01",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="MIA02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="MIA03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="MIA04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="MIA05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="MIA06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="MIA07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="MIA08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="MIA09",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount6: Optional[X12R] = element(
        name="MIA10",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount7: Optional[X12R] = element(
        name="MIA11",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount8: Optional[X12R] = element(
        name="MIA12",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount9: Optional[X12R] = element(
        name="MIA13",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount10: Optional[X12R] = element(
        name="MIA14",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity4: Optional[X12R] = element(
        name="MIA15",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount11: Optional[X12R] = element(
        name="MIA16",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount12: Optional[X12R] = element(
        name="MIA17",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount13: Optional[X12R] = element(
        name="MIA18",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount14: Optional[X12R] = element(
        name="MIA19",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="MIA20",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="MIA21",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification4: Optional[X12AN] = element(
        name="MIA22",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification5: Optional[X12AN] = element(
        name="MIA23",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    MonetaryAmount15: Optional[X12R] = element(
        name="MIA24",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
