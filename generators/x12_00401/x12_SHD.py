# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SHD(Segment):
    """
    SHD - Shipment Detail
    
    Description:
        To indicate shipment details in terms of quantity, weight, and routing instructions related to credit or debit of returned product
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SHD/
    """
    _id: Literal["SHD"] = id_element(name="SHD")

    NumberOfUnitsShipped: Optional[X12R] = element(
        name="SHD01",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    QuantityReceived: Optional[X12R] = element(
        name="SHD02",
        description="Quantity Received",
        min_length=1,
        max_length=7,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="SHD03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="SHD04",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="SHD05",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="SHD06",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="SHD07",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    OrderSizingFactor: Optional[X12R] = element(
        name="SHD08",
        description="Order Sizing Factor",
        min_length=1,
        max_length=10,
    )

    PriceBracketIdentifier: Optional[X12AN] = element(
        name="SHD09",
        description="Price Bracket Identifier",
        min_length=1,
        max_length=3,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="SHD10",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="SHD11",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ShipmentOrderStatusCode: Optional[X12ID] = element(
        name="SHD12",
        description="Shipment/Order Status Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="SHD13",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="SHD14",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
