# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BDD(Segment):
    """
    BDD - Beginning Segment for Shipment Delivery Discrepancy Information
    
    Description:
        To transmit identifying numbers and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BDD/
    """
    _id: Literal["BDD"] = id_element(name="BDD")

    InvoiceNumber: X12AN = element(
        name="BDD01",
        description="Invoice Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="BDD02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="BDD03",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )
