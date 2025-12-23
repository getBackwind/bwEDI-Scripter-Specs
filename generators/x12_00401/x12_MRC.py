# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class MRC(Segment):
    """
    MRC - Mortgagor Response Characteristics
    
    Description:
        To provide information on mortgagor responses and number of contacts made with a mortgagor
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MRC/
    """
    _id: Literal["MRC"] = id_element(name="MRC")

    EntityIdentifierCode: X12ID = element(
        name="MRC01",
        description="Entity Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    MortgagorResponseCode: X12ID = element(
        name="MRC02",
        description="Mortgagor Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ContactMethodCode: X12ID = element(
        name="MRC03",
        description="Contact Method Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Quantity: X12R = element(
        name="MRC04",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="MRC05",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    ContactMethodCode2: Optional[X12ID] = element(
        name="MRC06",
        description="Contact Method Code",
        min_length=1,
        max_length=1,
    )

    Quantity2: Optional[X12R] = element(
        name="MRC07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ContactMethodCode3: Optional[X12ID] = element(
        name="MRC08",
        description="Contact Method Code",
        min_length=1,
        max_length=1,
    )

    Quantity3: Optional[X12R] = element(
        name="MRC09",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
