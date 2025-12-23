# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class IS1(Segment):
    """
    IS1 - Estimated Time of Arrival and Car Scheduling
    
    Description:
        To transmit basic data relating to car scheduling information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IS1/
    """
    _id: Literal["IS1"] = id_element(name="IS1")

    TransactionSetPurposeCode: X12ID = element(
        name="IS101",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    EquipmentInitial: X12AN = element(
        name="IS102",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="IS103",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    LoadEmptyStatusCode: X12ID = element(
        name="IS104",
        description="Load/Empty Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RetripReasonCode: Optional[X12ID] = element(
        name="IS105",
        description="Retrip Reason Code",
        min_length=2,
        max_length=2,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="IS106",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    IndustryCode: Optional[X12AN] = element(
        name="IS107",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="IS108",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )
