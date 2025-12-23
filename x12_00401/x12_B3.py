# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class B3(Segment):
    """
    B3 - Beginning Segment for Carrier's Invoice
    
    Description:
        To transmit basic data relating to the carrier's invoice
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/B3/
    """
    _id: Literal["B3"] = id_element(name="B3")

    ShipmentQualifier: Optional[X12ID] = element(
        name="B301",
        description="Shipment Qualifier",
        min_length=1,
        max_length=1,
    )

    InvoiceNumber: X12AN = element(
        name="B302",
        description="Invoice Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="B303",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="B304",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="B305",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="B306",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    NetAmountDue: X12Nn = element(
        name="B307",
        description="Net Amount Due",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    CorrectionIndicator: Optional[X12ID] = element(
        name="B308",
        description="Correction Indicator",
    )

    DeliveryDate: Optional[X12DT] = element(
        name="B309",
        description="Delivery Date",
        min_length=8,
        max_length=8,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="B310",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="B311",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Date2: Optional[X12DT] = element(
        name="B312",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TariffServiceCode: Optional[X12ID] = element(
        name="B313",
        description="Tariff Service Code",
        min_length=2,
        max_length=2,
    )

    TransportationTermsCode: Optional[X12ID] = element(
        name="B314",
        description="Transportation Terms Code",
        min_length=3,
        max_length=3,
    )
