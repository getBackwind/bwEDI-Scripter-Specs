# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12Nn, X12R


class SVD(Segment):
    """
    SVD - Service Line Adjudication
    
    Description:
        To convey service line adjudication information for coordination of benefits between the initial payers of a health care claim and all subsequent payers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SVD/
    """
    _id: Literal["SVD"] = id_element(name="SVD")

    IdentificationCode: X12AN = element(
        name="SVD01",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    MonetaryAmount: X12R = element(
        name="SVD02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="SVD04",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Quantity: Optional[X12R] = element(
        name="SVD05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="SVD06",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )
