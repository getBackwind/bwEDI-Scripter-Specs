# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class PR2(Segment):
    """
    PR2 - Price Request Parameter List 2
    
    Description:
        To request price information based on certain parameters such as date, route, equipment type, and customer
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PR2/
    """
    _id: Literal["PR2"] = id_element(name="PR2")

    Date: Optional[X12DT] = element(
        name="PR201",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="PR202",
        description="Date",
        min_length=8,
        max_length=8,
    )

    RouteCode: Optional[X12AN] = element(
        name="PR203",
        description="Route Code",
        min_length=1,
        max_length=13,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="PR204",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="PR205",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="PR206",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PR207",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ConveyanceCode: Optional[X12ID] = element(
        name="PR208",
        description="Conveyance Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="PR209",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
