# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class M1(Segment):
    """
    M1 - Insurance
    
    Description:
        To specify details related to insurance
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/M1/
    """
    _id: Literal["M1"] = id_element(name="M1")

    CountryCode: X12ID = element(
        name="M101",
        description="Country Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    CarriageValue: Optional[X12Nn] = element(
        name="M102",
        description="Carriage Value",
        min_length=2,
        max_length=8,
    )

    DeclaredValue: Optional[X12Nn] = element(
        name="M103",
        description="Declared Value",
        min_length=2,
        max_length=12,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="M104",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="M105",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="M106",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="M107",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="M108",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentQualifier: Optional[X12ID] = element(
        name="M109",
        description="Percent Qualifier",
        min_length=1,
        max_length=2,
    )

    Percent: Optional[X12R] = element(
        name="M110",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    PercentQualifier2: Optional[X12ID] = element(
        name="M111",
        description="Percent Qualifier",
        min_length=1,
        max_length=2,
    )

    Percent2: Optional[X12R] = element(
        name="M112",
        description="Percent",
        min_length=1,
        max_length=10,
    )
