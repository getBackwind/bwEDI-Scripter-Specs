# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class EMP(Segment):
    """
    EMP - Employer
    
    Description:
        To provide employment specifics
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/EMP/
    """
    _id: Literal["EMP"] = id_element(name="EMP")

    Description: X12AN = element(
        name="EMP01",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="EMP02",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="EMP03",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="EMP04",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="EMP05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="EMP06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Description2: Optional[X12AN] = element(
        name="EMP07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="EMP08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="EMP09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="EMP10",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
