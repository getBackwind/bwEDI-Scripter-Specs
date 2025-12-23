# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class BT1(Segment):
    """
    BT1 - Batch Totals
    
    Description:
        To specify batch totals of monetary data elements, weights, or quantity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BT1/
    """
    _id: Literal["BT1"] = id_element(name="BT1")

    TransactionSetIdentifierCode: X12ID = element(
        name="BT101",
        description="Transaction Set Identifier Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    NumberOfTransactionSetsTotaled: X12Nn = element(
        name="BT102",
        description="Number of Transaction Sets Totaled",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    TotalQualifier: X12ID = element(
        name="BT103",
        description="Total Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DataElementTotaled: Optional[X12AN] = element(
        name="BT104",
        description="Data Element Totaled",
        min_length=4,
        max_length=5,
    )

    Total: X12R = element(
        name="BT105",
        description="Total",
        mandatory=True,
        min_length=1,
        max_length=11,
    )

    TotalQualifier2: Optional[X12ID] = element(
        name="BT106",
        description="Total Qualifier",
        min_length=1,
        max_length=1,
    )

    DataElementTotaled2: Optional[X12AN] = element(
        name="BT107",
        description="Data Element Totaled",
        min_length=4,
        max_length=5,
    )

    Total2: Optional[X12R] = element(
        name="BT108",
        description="Total",
        min_length=1,
        max_length=11,
    )

    TotalQualifier3: Optional[X12ID] = element(
        name="BT109",
        description="Total Qualifier",
        min_length=1,
        max_length=1,
    )

    DataElementTotaled3: Optional[X12AN] = element(
        name="BT110",
        description="Data Element Totaled",
        min_length=4,
        max_length=5,
    )

    Total3: Optional[X12R] = element(
        name="BT111",
        description="Total",
        min_length=1,
        max_length=11,
    )
