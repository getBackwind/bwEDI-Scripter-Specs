# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class PO3(Segment):
    """
    PO3 - Additional Item Detail
    
    Description:
        To specify additional item-related data involving variations in normal price/quantity structure
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PO3/
    """
    _id: Literal["PO3"] = id_element(name="PO3")

    ChangeReasonCode: X12ID = element(
        name="PO301",
        description="Change Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="PO302",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PriceIdentifierCode: Optional[X12ID] = element(
        name="PO303",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    UnitPrice: Optional[X12R] = element(
        name="PO304",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    BasisOfUnitPriceCode: Optional[X12ID] = element(
        name="PO305",
        description="Basis of Unit Price Code",
        min_length=2,
        max_length=2,
    )

    Quantity: X12R = element(
        name="PO306",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="PO307",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="PO308",
        description="Description",
        min_length=1,
        max_length=80,
    )
