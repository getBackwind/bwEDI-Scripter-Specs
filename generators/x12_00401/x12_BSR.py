# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BSR(Segment):
    """
    BSR - Beginning Segment for Order Status Report
    
    Description:
        To indicate the beginning of an Order Status Report Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BSR/
    """
    _id: Literal["BSR"] = id_element(name="BSR")

    StatusReportCode: X12ID = element(
        name="BSR01",
        description="Status Report Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ItemCode: X12ID = element(
        name="BSR02",
        description="Order/Item Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceID: X12AN = element(
        name="BSR03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BSR04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ProductDateCode: Optional[X12ID] = element(
        name="BSR05",
        description="Product/Date Code",
        min_length=2,
        max_length=2,
    )

    LocationCode: Optional[X12ID] = element(
        name="BSR06",
        description="Location Code",
        min_length=2,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="BSR07",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BSR08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date2: Optional[X12DT] = element(
        name="BSR09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="BSR10",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BSR11",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BSR12",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
