# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class CTT(Segment):
    """
    CTT - Transaction Totals
    
    Description:
        To transmit a hash total for a specific element in the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CTT/
    """
    _id: Literal["CTT"] = id_element(name="CTT")

    LineCount: X12Nn = element(
        name="CTT01",
        description="Number of Line Items",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    HashTotal: Optional[X12R] = element(
        name="CTT02",
        description="Hash Total",
        min_length=1,
        max_length=10,
    )

    Weight: Optional[X12R] = element(
        name="CTT03",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="CTT04",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="CTT05",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="CTT06",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="CTT07",
        description="Description",
        min_length=1,
        max_length=80,
    )
