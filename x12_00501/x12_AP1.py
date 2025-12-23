# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class AP1(Segment):
    """
    AP1 - Alternate Parts
    
    Description:
        To transmit identifying numbers, values and descriptive information related to the use of alternate parts
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AP1/
    """
    _id: Literal["AP1"] = id_element(name="AP1")

    ConditionIndicator: X12ID = element(
        name="AP101",
        description="Condition Indicator",
        mandatory=True,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="AP102",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    PriceIdentifierCode: Optional[X12ID] = element(
        name="AP103",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="AP104",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="AP105",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PostalCode: Optional[X12ID] = element(
        name="AP106",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    PostalCode2: Optional[X12ID] = element(
        name="AP107",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    PrintOptionCode: Optional[X12ID] = element(
        name="AP108",
        description="Print Option Code",
        min_length=2,
        max_length=2,
    )

    Number: Optional[X12Nn] = element(
        name="AP109",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Quantity: Optional[X12R] = element(
        name="AP110",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    FreeFormInformation: Optional[X12AN] = element(
        name="AP111",
        description="Free-form Information",
        min_length=1,
        max_length=30,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="AP112",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Description: Optional[X12AN] = element(
        name="AP113",
        description="Description",
        min_length=1,
        max_length=80,
    )
