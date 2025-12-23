# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MBL(Segment):
    """
    MBL - Bill of Lading
    
    Description:
        To specify a bill of lading number and associated information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MBL/
    """
    _id: Literal["MBL"] = id_element(name="MBL")

    StandardCarrierAlphaCode: X12ID = element(
        name="MBL01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    BillOfLadingWaybillNumber: X12AN = element(
        name="MBL02",
        description="Bill of Lading/Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    ActionCode: Optional[X12ID] = element(
        name="MBL03",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="MBL04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    TypeOfServiceCode: Optional[X12ID] = element(
        name="MBL05",
        description="Type of Service Code",
        min_length=2,
        max_length=2,
    )
