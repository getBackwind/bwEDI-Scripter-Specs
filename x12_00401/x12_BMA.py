# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class BMA(Segment):
    """
    BMA - Beginning Segment for Market Development Fund Allocation
    
    Description:
        To indicate identifying numbers, dates, and other basic data relative to market development funds
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BMA/
    """
    _id: Literal["BMA"] = id_element(name="BMA")

    TransactionSetPurposeCode: X12ID = element(
        name="BMA01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="BMA02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    AllowanceOrChargeMethodOfHandlingCode: X12ID = element(
        name="BMA03",
        description="Allowance or Charge Method of Handling Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BMA04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: X12DT = element(
        name="BMA05",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    TransactionTypeCode: X12ID = element(
        name="BMA06",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="BMA07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Description: Optional[X12AN] = element(
        name="BMA08",
        description="Description",
        min_length=1,
        max_length=80,
    )
