# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DD(Segment):
    """
    DD - Demand Detail
    
    Description:
        To describe the type of demand and the intended use of material
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DD/
    """
    _id: Literal["DD"] = id_element(name="DD")

    IndustryCode: Optional[X12AN] = element(
        name="DD01",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="DD02",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="DD03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="DD04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="DD05",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    CodeListQualifierCode2: Optional[X12ID] = element(
        name="DD06",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    Quantity: Optional[X12R] = element(
        name="DD07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="DD08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    IndustryCode3: Optional[X12AN] = element(
        name="DD09",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    CodeListQualifierCode3: Optional[X12ID] = element(
        name="DD10",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )
