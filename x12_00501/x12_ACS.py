# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class ACS(Segment):
    """
    ACS - Ancillary Charges
    
    Description:
        To identify additional charges and payment terms for shipment charges that may or may not be directly related to a line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ACS/
    """
    _id: Literal["ACS"] = id_element(name="ACS")

    Amount: X12Nn = element(
        name="ACS01",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    SpecialChargeOrAllowanceCode: X12ID = element(
        name="ACS02",
        description="Special Charge or Allowance Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Description: Optional[X12AN] = element(
        name="ACS03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ShipmentMethodOfPayment: Optional[X12ID] = element(
        name="ACS04",
        description="Shipment Method of Payment",
    )
