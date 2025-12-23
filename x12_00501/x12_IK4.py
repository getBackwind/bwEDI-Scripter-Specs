# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class IK4(Segment):
    """
    IK4 - Implementation Data Element Note
    
    Description:
        To report implementation errors in a data element or composite data structure and identify the location of the data element
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IK4/
    """
    _id: Literal["IK4"] = id_element(name="IK4")

    DataElementReferenceNumber: Optional[X12Nn] = element(
        name="IK402",
        description="Data Element Reference Number",
        min_length=1,
        max_length=4,
    )

    ImplementationDataElementSyntaxErrorCode: X12ID = element(
        name="IK403",
        description="Implementation Data Element Syntax Error Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    CopyOfBadDataElement: Optional[X12AN] = element(
        name="IK404",
        description="Copy of Bad Data Element",
        min_length=1,
        max_length=99,
    )
