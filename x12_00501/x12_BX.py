# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BX(Segment):
    """
    BX - General Shipment Information
    
    Description:
        To transmit identification numbers and other basic shipment data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BX/
    """
    _id: Literal["BX"] = id_element(name="BX")

    TransactionSetPurposeCode: X12ID = element(
        name="BX01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TransportationMethodTypeCode: X12ID = element(
        name="BX02",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="BX03",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="BX04",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="BX05",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="BX06",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    ShipmentQualifier: Optional[X12ID] = element(
        name="BX07",
        description="Shipment Qualifier",
        min_length=1,
        max_length=1,
    )

    SectionSevenCode: Optional[X12ID] = element(
        name="BX08",
        description="Section Seven Code",
        min_length=1,
        max_length=1,
    )

    CapacityLoadCode: Optional[X12ID] = element(
        name="BX09",
        description="Capacity Load Code",
        min_length=1,
        max_length=1,
    )

    StatusReportRequestCode: Optional[X12ID] = element(
        name="BX10",
        description="Status Report Request Code",
        min_length=1,
        max_length=1,
    )

    CustomsDocumentationHandlingCode: Optional[X12ID] = element(
        name="BX11",
        description="Customs Documentation Handling Code",
        min_length=2,
        max_length=2,
    )

    ConfidentialBillingRequestCode: Optional[X12ID] = element(
        name="BX12",
        description="Confidential Billing Request Code",
        min_length=1,
        max_length=1,
    )

    GoodsAndServicesTaxReasonCode: Optional[X12ID] = element(
        name="BX13",
        description="Goods and Services Tax Reason Code",
        min_length=1,
        max_length=1,
    )

    ApplicationType: Optional[X12ID] = element(
        name="BX14",
        description="Application Type",
    )
