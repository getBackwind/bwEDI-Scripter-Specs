# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class W06(Segment):
    """
    W06 - Warehouse Shipment Identification
    
    Description:
        To provide identifying numbers, dates, and other basic data for this transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W06/
    """
    _id: Literal["W06"] = id_element(name="W06")

    ReportingCode: X12ID = element(
        name="W0601",
        description="Reporting Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DepositorOrderNumber: Optional[X12AN] = element(
        name="W0602",
        description="Depositor Order Number",
        min_length=1,
        max_length=22,
    )

    Date: Optional[X12DT] = element(
        name="W0603",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="W0604",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    AgentShipmentIDNumber: Optional[X12AN] = element(
        name="W0605",
        description="Agent Shipment ID Number",
        min_length=1,
        max_length=12,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="W0606",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    MasterReferenceLinkNumber: Optional[X12AN] = element(
        name="W0607",
        description="Master Reference (Link) Number",
        min_length=1,
        max_length=22,
    )

    LinkSequenceNumber: Optional[X12Nn] = element(
        name="W0608",
        description="Link Sequence Number",
        min_length=6,
        max_length=6,
    )

    SpecialHandlingCode: Optional[X12ID] = element(
        name="W0609",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    ShippingDateChangeReasonCode: Optional[X12ID] = element(
        name="W0610",
        description="Shipping Date Change Reason Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="W0611",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="W0612",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
