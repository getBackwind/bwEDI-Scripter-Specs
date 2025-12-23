# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class N4(Segment):
    """
    N4 - Geographic Location
    
    Description:
        To specify the geographic place of the named party
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/N4/
    """
    _id: Literal["N4"] = id_element(name="N4")

    City: Optional[X12AN] = element(
        name="N401",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    State: Optional[X12ID] = element(
        name="N402",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    PostalCode: Optional[X12ID] = element(
        name="N403",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    Country: Optional[X12ID] = element(
        name="N404",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="N405",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="N406",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )
