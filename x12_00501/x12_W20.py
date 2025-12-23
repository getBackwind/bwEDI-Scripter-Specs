# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class W20(Segment):
    """
    W20 - Line Item Detail - Packing
    
    Description:
        To specify packing details of the items shipped
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W20/
    """
    _id: Literal["W20"] = id_element(name="W20")

    Pack: Optional[X12Nn] = element(
        name="W2001",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    Size: Optional[X12R] = element(
        name="W2002",
        description="Size",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="W2003",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="W2004",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="W2005",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="W2006",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    UnitWeight: Optional[X12R] = element(
        name="W2007",
        description="Unit Weight",
        min_length=1,
        max_length=8,
    )

    Volume: Optional[X12R] = element(
        name="W2008",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="W2009",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Color: Optional[X12AN] = element(
        name="W2010",
        description="Color",
        min_length=1,
        max_length=10,
    )
