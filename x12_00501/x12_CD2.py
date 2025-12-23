# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CD2(Segment):
    """
    CD2 - Multi-Valued Characteristics
    
    Description:
        To provide characteristics that may have multiple values
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CD2/
    """
    _id: Literal["CD2"] = id_element(name="CD2")

    CodeCategory: X12ID = element(
        name="CD201",
        description="Code Category",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceIDQualifier: X12ID = element(
        name="CD202",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MedicalCodeValue: X12AN = element(
        name="CD203",
        description="Medical Code Value",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    MedicalCodeValue2: Optional[X12AN] = element(
        name="CD204",
        description="Medical Code Value",
        min_length=1,
        max_length=15,
    )

    MedicalCodeValue3: Optional[X12AN] = element(
        name="CD205",
        description="Medical Code Value",
        min_length=1,
        max_length=15,
    )

    MedicalCodeValue4: Optional[X12AN] = element(
        name="CD206",
        description="Medical Code Value",
        min_length=1,
        max_length=15,
    )

    MedicalCodeValue5: Optional[X12AN] = element(
        name="CD207",
        description="Medical Code Value",
        min_length=1,
        max_length=15,
    )

    MedicalCodeValue6: Optional[X12AN] = element(
        name="CD208",
        description="Medical Code Value",
        min_length=1,
        max_length=15,
    )
