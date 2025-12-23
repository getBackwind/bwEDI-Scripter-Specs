# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class G93(Segment):
    """
    G93 - Price Bracket Identification
    
    Description:
        To identify price bracket values
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G93/
    """
    _id: Literal["G93"] = id_element(name="G93")

    PriceBracketIdentifier: Optional[X12AN] = element(
        name="G9301",
        description="Price Bracket Identifier",
        min_length=1,
        max_length=3,
    )

    Quantity: Optional[X12R] = element(
        name="G9302",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G9303",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="G9304",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="G9305",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    PriceIdentifierCode: Optional[X12ID] = element(
        name="G9306",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    ActionCode: Optional[X12ID] = element(
        name="G9307",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="G9308",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
