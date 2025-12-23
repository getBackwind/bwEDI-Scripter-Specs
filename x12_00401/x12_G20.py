# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G20(Segment):
    """
    G20 - Item Packing Detail
    
    Description:
        To specify packing details of the items shipped
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G20/
    """
    _id: Literal["G20"] = id_element(name="G20")

    Pack: Optional[X12Nn] = element(
        name="G2001",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    Size: Optional[X12R] = element(
        name="G2002",
        description="Size",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G2003",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="G2004",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="G2005",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="G2006",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="G2007",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Color: Optional[X12AN] = element(
        name="G2008",
        description="Color",
        min_length=1,
        max_length=10,
    )

    InnerPack: Optional[X12Nn] = element(
        name="G2009",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )
