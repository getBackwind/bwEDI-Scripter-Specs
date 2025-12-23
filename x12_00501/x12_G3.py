# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G3(Segment):
    """
    G3 - Compensation Information
    
    Description:
        To convey brokerage, freight forwarder compensation, and other compensation information related to shipments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G3/
    """
    _id: Literal["G3"] = id_element(name="G3")

    CompensationPaid: Optional[X12R] = element(
        name="G301",
        description="Compensation Paid",
        min_length=2,
        max_length=5,
    )

    TotalCompensationAmount: X12Nn = element(
        name="G302",
        description="Total Compensation Amount",
        mandatory=True,
        min_length=3,
        max_length=10,
    )

    Name: Optional[X12AN] = element(
        name="G303",
        description="Name",
        min_length=1,
        max_length=60,
    )

    BusinessTransactionStatus: Optional[X12ID] = element(
        name="G304",
        description="Business Transaction Status",
    )

    MonetaryAmount: Optional[X12R] = element(
        name="G305",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    CompensationQualifier: Optional[X12ID] = element(
        name="G306",
        description="Compensation Qualifier",
        min_length=1,
        max_length=1,
    )
