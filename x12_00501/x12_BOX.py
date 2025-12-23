# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class BOX(Segment):
    """
    BOX - Box Office Detail
    
    Description:
        To provide detail information regarding a specific event
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BOX/
    """
    _id: Literal["BOX"] = id_element(name="BOX")

    FrequencyCode: X12ID = element(
        name="BOX01",
        description="Frequency Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ShowCode: X12ID = element(
        name="BOX02",
        description="Show Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TicketCategoryCode: X12ID = element(
        name="BOX03",
        description="Ticket Category Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: X12R = element(
        name="BOX04",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="BOX05",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="BOX06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="BOX07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="BOX08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="BOX09",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity4: Optional[X12R] = element(
        name="BOX10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="BOX11",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    UnitPrice: Optional[X12R] = element(
        name="BOX12",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="BOX13",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BOX14",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BOX15",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
