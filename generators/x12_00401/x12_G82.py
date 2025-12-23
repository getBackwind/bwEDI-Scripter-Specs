# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class G82(Segment):
    """
    G82 - Delivery/Return Base Record Identifier
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G82/
    """
    _id: Literal["G82"] = id_element(name="G82")

    CreditDebitFlagCode: X12ID = element(
        name="G8201",
        description="Credit/Debit Flag Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    SupplierSDeliveryReturnNumber: X12AN = element(
        name="G8202",
        description="Supplier's Delivery/Return Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    DUNSNumber: X12ID = element(
        name="G8203",
        description="D-U-N-S Number",
        mandatory=True,
        min_length=9,
        max_length=9,
    )

    ReceiverSLocationNumber: X12AN = element(
        name="G8204",
        description="Receiver's Location Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    DUNSNumber2: X12ID = element(
        name="G8205",
        description="D-U-N-S Number",
        mandatory=True,
        min_length=9,
        max_length=9,
    )

    SupplierSLocationNumber: X12AN = element(
        name="G8206",
        description="Supplier's Location Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    PhysicalDeliveryOrReturnDate: X12DT = element(
        name="G8207",
        description="Physical Delivery or Return Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ProductOwnershipTransferDate: Optional[X12DT] = element(
        name="G8208",
        description="Product Ownership Transfer Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="G8209",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    PurchaseOrderDate: Optional[X12DT] = element(
        name="G8210",
        description="Purchase Order Date",
        min_length=8,
        max_length=8,
    )

    ShipmentMethodOfPayment: Optional[X12ID] = element(
        name="G8211",
        description="Shipment Method of Payment",
    )

    CODMethodOfPaymentCode: Optional[X12ID] = element(
        name="G8212",
        description="COD Method of Payment Code",
        min_length=1,
        max_length=1,
    )
