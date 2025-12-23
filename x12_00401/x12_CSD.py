# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class CSD(Segment):
    """
    CSD - Consolidated Shipment Invoice Data
    
    Description:
        To specify the data relative to carrier invoices on consolidated shipments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CSD/
    """
    _id: Literal["CSD"] = id_element(name="CSD")

    SpecialHandlingCode: X12ID = element(
        name="CSD01",
        description="Special Handling Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="CSD02",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="CSD03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="CSD04",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    Date: X12DT = element(
        name="CSD05",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: X12DT = element(
        name="CSD06",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Charge: X12Nn = element(
        name="CSD07",
        description="Charge",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="CSD08",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="CSD09",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
