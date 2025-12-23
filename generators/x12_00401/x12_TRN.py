# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TRN(Segment):
    """
    TRN - Trace
    
    Description:
        To uniquely identify a transaction to an application
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TRN/
    """
    _id: Literal["TRN"] = id_element(name="TRN")

    TraceTypeCode: X12ID = element(
        name="TRN01",
        description="Trace Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: X12AN = element(
        name="TRN02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    OriginatingCompanyIdentifier: Optional[X12AN] = element(
        name="TRN03",
        description="Originating Company Identifier",
        min_length=10,
        max_length=10,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="TRN04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
