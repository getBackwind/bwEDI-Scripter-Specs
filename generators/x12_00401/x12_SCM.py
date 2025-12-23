# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class SCM(Segment):
    """
    SCM - Credit Score Model
    
    Description:
        To define the credit score model used and the related score
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SCM/
    """
    _id: Literal["SCM"] = id_element(name="SCM")

    ProductServiceID: Optional[X12AN] = element(
        name="SCM01",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Number: Optional[X12Nn] = element(
        name="SCM02",
        description="Number",
        min_length=1,
        max_length=9,
    )

    EvaluationRatingCode: Optional[X12ID] = element(
        name="SCM03",
        description="Evaluation Rating Code",
        min_length=1,
        max_length=1,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="SCM04",
        description="Free Form Message",
        min_length=1,
        max_length=60,
    )
