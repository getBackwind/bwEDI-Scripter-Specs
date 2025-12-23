# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class W05(Segment):
    """
    W05 - Shipping Order Identification
    
    Description:
        To transmit identifying numbers and other basic data for this transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W05/
    """
    _id: Literal["W05"] = id_element(name="W05")

    OrderStatusCode: X12ID = element(
        name="W0501",
        description="Order Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DepositorOrderNumber: X12AN = element(
        name="W0502",
        description="Depositor Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="W0503",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    LinkSequenceNumber: Optional[X12Nn] = element(
        name="W0504",
        description="Link Sequence Number",
        min_length=6,
        max_length=6,
    )

    MasterReferenceLinkNumber: Optional[X12AN] = element(
        name="W0505",
        description="Master Reference (Link) Number",
        min_length=1,
        max_length=22,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="W0506",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="W0507",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    PurchaseOrderTypeCode: Optional[X12ID] = element(
        name="W0508",
        description="Purchase Order Type Code",
        min_length=2,
        max_length=2,
    )
