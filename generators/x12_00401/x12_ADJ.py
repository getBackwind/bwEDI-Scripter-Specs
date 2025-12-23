# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class ADJ(Segment):
    """
    ADJ - Adjustments to Balances or Services
    
    Description:
        To identify adjustments to account balances or service charges on the account
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ADJ/
    """
    _id: Literal["ADJ"] = id_element(name="ADJ")

    AdjustmentApplicationCode: X12ID = element(
        name="ADJ01",
        description="Adjustment Application Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    MonetaryAmount: X12R = element(
        name="ADJ02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="ADJ03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Date: X12DT = element(
        name="ADJ04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: X12DT = element(
        name="ADJ05",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Number: Optional[X12Nn] = element(
        name="ADJ06",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Description: Optional[X12AN] = element(
        name="ADJ07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="ADJ08",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="ADJ09",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Amount: Optional[X12Nn] = element(
        name="ADJ10",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount2: Optional[X12Nn] = element(
        name="ADJ11",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount3: Optional[X12Nn] = element(
        name="ADJ12",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Quantity: Optional[X12R] = element(
        name="ADJ13",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="ADJ14",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="ADJ15",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="ADJ16",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ADJ17",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
