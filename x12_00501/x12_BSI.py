# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BSI(Segment):
    """
    BSI - Beginning Segment for Order Status Inquiry
    
    Description:
        To indicate the beginning of an order status inquiry and provide the type of customer status inquiry
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BSI/
    """
    _id: Literal["BSI"] = id_element(name="BSI")

    ReferenceIdentification: X12AN = element(
        name="BSI01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: X12DT = element(
        name="BSI02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    OrderItemCode: X12ID = element(
        name="BSI03",
        description="Order/Item Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductDateCode: Optional[X12ID] = element(
        name="BSI04",
        description="Product/Date Code",
        min_length=2,
        max_length=2,
    )

    LocationCode: Optional[X12ID] = element(
        name="BSI05",
        description="Location Code",
        min_length=2,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="BSI06",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BSI07",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BSI08",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BSI09",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
