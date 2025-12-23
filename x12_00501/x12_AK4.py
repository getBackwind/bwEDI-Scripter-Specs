# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class AK4(Segment):
    """
    AK4 - Data Element Note
    
    Description:
        To report errors in a data element or composite data structure and identify the location of the data element
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AK4/
    """
    _id: Literal["AK4"] = id_element(name="AK4")

    ElementReferenceID: Optional[X12Nn] = element(
        name="AK402",
        description="Data Element Reference Number",
        min_length=1,
        max_length=4,
    )

    ErrorCode: X12ID = element(
        name="AK403",
        description="Data Element Syntax Error Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ElementCopy: Optional[X12AN] = element(
        name="AK404",
        description="Copy of Bad Data Element",
        min_length=1,
        max_length=99,
    )
