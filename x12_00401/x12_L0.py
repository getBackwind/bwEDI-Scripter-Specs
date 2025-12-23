# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class L0(Segment):
    """
    L0 - Line Item - Quantity and Weight
    
    Description:
        To specify quantity, weight, volume, and type of service for a line item including applicable "quantity/rate-as"data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/L0/
    """
    _id: Literal["L0"] = id_element(name="L0")

    LadingLineItemNumber: Optional[X12Nn] = element(
        name="L001",
        description="Lading Line Item Number",
        min_length=1,
        max_length=3,
    )

    BilledRatedAsQuantity: Optional[X12R] = element(
        name="L002",
        description="Billed/Rated-as Quantity",
        min_length=1,
        max_length=11,
    )

    BilledRatedAsQualifier: Optional[X12ID] = element(
        name="L003",
        description="Billed/Rated-as Qualifier",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="L004",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="L005",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="L006",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="L007",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="L008",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    PackagingFormCode: Optional[X12ID] = element(
        name="L009",
        description="Packaging Form Code",
        min_length=3,
        max_length=3,
    )

    DunnageDescription: Optional[X12AN] = element(
        name="L010",
        description="Dunnage Description",
        min_length=2,
        max_length=25,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="L011",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    TypeOfServiceCode: Optional[X12ID] = element(
        name="L012",
        description="Type of Service Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="L013",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PackagingFormCode2: Optional[X12ID] = element(
        name="L014",
        description="Packaging Form Code",
        min_length=3,
        max_length=3,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="L015",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
