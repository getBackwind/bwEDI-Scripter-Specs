# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class JIL(Segment):
    """
    JIL - Line Item Detail for the Operating Expense Statement
    
    Description:
        To specify the service code or classification the expense will be charged to and provide the required expense data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/JIL/
    """
    _id: Literal["JIL"] = id_element(name="JIL")

    ProductServiceIDQualifier: X12ID = element(
        name="JIL01",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="JIL02",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="JIL03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="JIL04",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="JIL05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date: Optional[X12DT] = element(
        name="JIL06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="JIL07",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )
