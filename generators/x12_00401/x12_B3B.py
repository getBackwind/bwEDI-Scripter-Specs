# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class B3B(Segment):
    """
    B3B - Beginning Segment for Carrier's Invoice
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/B3B/
    """
    _id: Literal["B3B"] = id_element(name="B3B")

    InvoiceNumber: X12AN = element(
        name="B3B01",
        description="Invoice Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="B3B02",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    Date: X12DT = element(
        name="B3B03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    NetAmountDue: X12Nn = element(
        name="B3B04",
        description="Net Amount Due",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    Date2: Optional[X12DT] = element(
        name="B3B05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="B3B06",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    TransportationMethodTypeCode: X12ID = element(
        name="B3B07",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="B3B08",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="B3B09",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    CorrectionIndicator: Optional[X12ID] = element(
        name="B3B10",
        description="Correction Indicator",
    )

    CurrencyCode: Optional[X12ID] = element(
        name="B3B11",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
