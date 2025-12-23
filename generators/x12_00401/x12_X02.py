# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class X02(Segment):
    """
    X02 - Automated Manifest Bills Eligible/Overdue Archive Details
    
    Description:
        To specify bills of lading overdue archive
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/X02/
    """
    _id: Literal["X02"] = id_element(name="X02")

    StandardCarrierAlphaCode: X12ID = element(
        name="X0201",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: X12ID = element(
        name="X0202",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    BillOfLadingWaybillNumber: X12AN = element(
        name="X0203",
        description="Bill of Lading/Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="X0204",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    BillOfLadingWaybillNumber2: Optional[X12AN] = element(
        name="X0205",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=12,
    )
