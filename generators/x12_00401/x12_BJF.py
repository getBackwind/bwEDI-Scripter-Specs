# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BJF(Segment):
    """
    BJF - Beginning Segment Railroad Junctions and Interchanges Update Activity
    
    Description:
        To define the purpose, junction and standard point location code for the Railroad Junctions and Interchanges Update Activity Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BJF/
    """
    _id: Literal["BJF"] = id_element(name="BJF")

    TransactionSetPurposeCode: X12ID = element(
        name="BJF01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: X12ID = element(
        name="BJF02",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Rule260JunctionCode: X12ID = element(
        name="BJF03",
        description="Rule 260 Junction Code",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="BJF04",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    CityName: Optional[X12AN] = element(
        name="BJF05",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="BJF06",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="BJF07",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
