# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12R


class TS3(Segment):
    """
    TS3 - Transaction Statistics
    
    Description:
        To supply provider-level control information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TS3/
    """
    _id: Literal["TS3"] = id_element(name="TS3")

    ReferenceIdentification: X12AN = element(
        name="TS301",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    FacilityCodeValue: X12AN = element(
        name="TS302",
        description="Facility Code Value",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Date: X12DT = element(
        name="TS303",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Quantity: X12R = element(
        name="TS304",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: X12R = element(
        name="TS305",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="TS306",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="TS307",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="TS308",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="TS309",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount6: Optional[X12R] = element(
        name="TS310",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount7: Optional[X12R] = element(
        name="TS311",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount8: Optional[X12R] = element(
        name="TS312",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount9: Optional[X12R] = element(
        name="TS313",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount10: Optional[X12R] = element(
        name="TS314",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount11: Optional[X12R] = element(
        name="TS315",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount12: Optional[X12R] = element(
        name="TS316",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount13: Optional[X12R] = element(
        name="TS317",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount14: Optional[X12R] = element(
        name="TS318",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount15: Optional[X12R] = element(
        name="TS319",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount16: Optional[X12R] = element(
        name="TS320",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount17: Optional[X12R] = element(
        name="TS321",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount18: Optional[X12R] = element(
        name="TS322",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity2: Optional[X12R] = element(
        name="TS323",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount19: Optional[X12R] = element(
        name="TS324",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
