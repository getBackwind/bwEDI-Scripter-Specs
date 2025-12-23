# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class CF2(Segment):
    """
    CF2 - Summary Freight Bill Detail
    
    Description:
        To identify the freight bill number, net amount due, and other basic data related to the freight bill such as date of pickup
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CF2/
    """
    _id: Literal["CF2"] = id_element(name="CF2")

    InvoiceNumber: X12AN = element(
        name="CF201",
        description="Invoice Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    NetAmountDue: X12Nn = element(
        name="CF202",
        description="Net Amount Due",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="CF203",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    ShipmentMethodOfPayment: Optional[X12ID] = element(
        name="CF204",
        description="Shipment Method of Payment",
    )

    Date: Optional[X12DT] = element(
        name="CF205",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="CF206",
        description="Date",
        min_length=8,
        max_length=8,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="CF207",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="CF208",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="CF209",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="CF210",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
