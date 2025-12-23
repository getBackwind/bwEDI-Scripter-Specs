# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class SCN(Segment):
    """
    SCN - Beginning Segment for Cartage Work Assignment
    
    Description:
        To indicate the beginning of the Cartage Work Assignment Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SCN/
    """
    _id: Literal["SCN"] = id_element(name="SCN")

    StandardCarrierAlphaCode: X12ID = element(
        name="SCN01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    ReferenceIdentification: X12AN = element(
        name="SCN02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    TransactionSetPurposeCode: X12ID = element(
        name="SCN03",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="SCN04",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    Amount: Optional[X12Nn] = element(
        name="SCN05",
        description="Amount",
        min_length=1,
        max_length=15,
    )
