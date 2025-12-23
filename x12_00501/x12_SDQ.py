# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SDQ(Segment):
    """
    SDQ - Destination Quantity
    
    Description:
        To specify destination and quantity detail
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SDQ/
    """
    _id: Literal["SDQ"] = id_element(name="SDQ")

    UOM: X12ID = element(
        name="SDQ01",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    IdCodeQualifier: Optional[X12ID] = element(
        name="SDQ02",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdCode: X12AN = element(
        name="SDQ03",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    Quantity: X12R = element(
        name="SDQ04",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    IdCode2: Optional[X12AN] = element(
        name="SDQ05",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity2: Optional[X12R] = element(
        name="SDQ06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode3: Optional[X12AN] = element(
        name="SDQ07",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity3: Optional[X12R] = element(
        name="SDQ08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode4: Optional[X12AN] = element(
        name="SDQ09",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity4: Optional[X12R] = element(
        name="SDQ10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode5: Optional[X12AN] = element(
        name="SDQ11",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity5: Optional[X12R] = element(
        name="SDQ12",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode6: Optional[X12AN] = element(
        name="SDQ13",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity6: Optional[X12R] = element(
        name="SDQ14",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode7: Optional[X12AN] = element(
        name="SDQ15",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity7: Optional[X12R] = element(
        name="SDQ16",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode8: Optional[X12AN] = element(
        name="SDQ17",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity8: Optional[X12R] = element(
        name="SDQ18",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode9: Optional[X12AN] = element(
        name="SDQ19",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity9: Optional[X12R] = element(
        name="SDQ20",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IdCode10: Optional[X12AN] = element(
        name="SDQ21",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity10: Optional[X12R] = element(
        name="SDQ22",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="SDQ23",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )
