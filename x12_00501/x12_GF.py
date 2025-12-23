# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class GF(Segment):
    """
    GF - Furnished Goods and Services
    
    Description:
        To specify information related to furnished material, equipment, property, information, and services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/GF/
    """
    _id: Literal["GF"] = id_element(name="GF")

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="GF01",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="GF02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ContractNumber: Optional[X12AN] = element(
        name="GF03",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="GF04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="GF05",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="GF06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="GF07",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier3: Optional[X12ID] = element(
        name="GF08",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="GF09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
