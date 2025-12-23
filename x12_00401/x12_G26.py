# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R


class G26(Segment):
    """
    G26 - Pricing Conditions
    
    Description:
        To specify vendor's conditions related to price change
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G26/
    """
    _id: Literal["G26"] = id_element(name="G26")

    PriceConditionCode: X12ID = element(
        name="G2601",
        description="Price Condition Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateQualifier: Optional[X12ID] = element(
        name="G2602",
        description="Date Qualifier",
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="G2603",
        description="Date",
        min_length=8,
        max_length=8,
    )

    QuantityBasis: Optional[X12ID] = element(
        name="G2604",
        description="Quantity Basis",
    )

    Quantity: Optional[X12R] = element(
        name="G2605",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G2606",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
