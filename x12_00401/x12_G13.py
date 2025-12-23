# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class G13(Segment):
    """
    G13 - Store Size Attributes
    
    Description:
        To indicate the type and size characteristics of a retail store
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G13/
    """
    _id: Literal["G13"] = id_element(name="G13")

    ClassOfTradeCode: X12ID = element(
        name="G1301",
        description="Class of Trade Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="G1302",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G1303",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Number: Optional[X12Nn] = element(
        name="G1304",
        description="Number",
        min_length=1,
        max_length=9,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="G1305",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="G1306",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )
