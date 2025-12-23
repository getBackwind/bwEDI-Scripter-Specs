# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class UDA(Segment):
    """
    UDA - Underwriting Condition
    
    Description:
        To specify the condition under which insurance coverage is offered
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/UDA/
    """
    _id: Literal["UDA"] = id_element(name="UDA")

    OfferBasisCode: X12ID = element(
        name="UDA01",
        description="Offer Basis Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="UDA02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="UDA03",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="UDA04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="UDA05",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="UDA06",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="UDA07",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
