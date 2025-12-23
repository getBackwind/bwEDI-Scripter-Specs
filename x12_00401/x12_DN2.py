# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DN2(Segment):
    """
    DN2 - Tooth Summary
    
    Description:
        To specify the status of individual teeth
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DN2/
    """
    _id: Literal["DN2"] = id_element(name="DN2")

    ReferenceIdentification: X12AN = element(
        name="DN201",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    ToothStatusCode: X12ID = element(
        name="DN202",
        description="Tooth Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="DN203",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="DN204",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="DN205",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )
