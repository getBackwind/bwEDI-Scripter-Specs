# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G40(Segment):
    """
    G40 - Bracket Price
    
    Description:
        To provide a vendor's pricing structure associated with a specific line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G40/
    """
    _id: Literal["G40"] = id_element(name="G40")

    PriceBracketIdentifier: Optional[X12AN] = element(
        name="G4001",
        description="Price Bracket Identifier",
        min_length=1,
        max_length=3,
    )

    ItemListCostNew: X12R = element(
        name="G4002",
        description="Item List Cost - New",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    ItemListCostOld: Optional[X12R] = element(
        name="G4003",
        description="Item List Cost - Old",
        min_length=1,
        max_length=9,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="G4004",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    PriceNewSuggestedRetail: Optional[X12Nn] = element(
        name="G4005",
        description="Price New, Suggested Retail",
        min_length=2,
        max_length=7,
    )

    PriceOldSuggestedRetail: Optional[X12Nn] = element(
        name="G4006",
        description="Price Old, Suggested Retail",
        min_length=2,
        max_length=7,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G4007",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PriceIdentifierCode: Optional[X12ID] = element(
        name="G4008",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    Number: Optional[X12Nn] = element(
        name="G4009",
        description="Number",
        min_length=1,
        max_length=9,
    )
