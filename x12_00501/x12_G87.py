# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class G87(Segment):
    """
    G87 - Delivery/Return Adjustment Identification
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G87/
    """
    _id: Literal["G87"] = id_element(name="G87")

    InitiatorCode: X12ID = element(
        name="G8701",
        description="Initiator Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CreditDebitFlagCode: X12ID = element(
        name="G8702",
        description="Credit/Debit Flag Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    SupplierSDeliveryReturnNumber: X12AN = element(
        name="G8703",
        description="Supplier's Delivery/Return Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    IntegrityCheckValue: X12AN = element(
        name="G8704",
        description="Integrity Check Value",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    AdjustmentSequenceNumber: X12Nn = element(
        name="G8705",
        description="Adjustment Sequence Number",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReceiverDeliveryReturnNumber: Optional[X12AN] = element(
        name="G8706",
        description="Receiver Delivery/Return Number",
        min_length=1,
        max_length=22,
    )
