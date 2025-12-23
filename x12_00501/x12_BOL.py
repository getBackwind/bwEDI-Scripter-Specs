# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BOL(Segment):
    """
    BOL - Beginning Segment for the Motor Carrier Bill of Lading
    
    Description:
        To transmit identifying numbers, dates, and other basic data related to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BOL/
    """
    _id: Literal["BOL"] = id_element(name="BOL")

    StandardCarrierAlphaCode: X12ID = element(
        name="BOL01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="BOL02",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    ShipmentIdentificationNumber: X12AN = element(
        name="BOL03",
        description="Shipment Identification Number",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BOL04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BOL05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BOL06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    StatusReportRequestCode: Optional[X12ID] = element(
        name="BOL07",
        description="Status Report Request Code",
        min_length=1,
        max_length=1,
    )

    SectionSevenCode: Optional[X12ID] = element(
        name="BOL08",
        description="Section Seven Code",
        min_length=1,
        max_length=1,
    )

    CustomsDocumentationHandlingCode: Optional[X12ID] = element(
        name="BOL09",
        description="Customs Documentation Handling Code",
        min_length=2,
        max_length=2,
    )

    ShipmentMethodOfPayment2: Optional[X12ID] = element(
        name="BOL10",
        description="Shipment Method of Payment",
    )

    CurrencyCode: Optional[X12ID] = element(
        name="BOL11",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
