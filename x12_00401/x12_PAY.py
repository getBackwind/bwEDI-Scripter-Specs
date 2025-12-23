# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class PAY(Segment):
    """
    PAY - Adjustable Payment Description
    
    Description:
        To provide the terms of payment adjustment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PAY/
    """
    _id: Literal["PAY"] = id_element(name="PAY")

    PaymentAdjustmentCode: X12ID = element(
        name="PAY01",
        description="Payment Adjustment Code",
        mandatory=True,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PAY02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12R] = element(
        name="PAY03",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="PAY04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent2: Optional[X12R] = element(
        name="PAY05",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="PAY06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="PAY08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="PAY10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Percent3: Optional[X12R] = element(
        name="PAY11",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    Percent4: Optional[X12R] = element(
        name="PAY12",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="PAY13",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PAY14",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Quantity3: Optional[X12R] = element(
        name="PAY15",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Percent5: Optional[X12R] = element(
        name="PAY16",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="PAY17",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    NegativeAmortizationQualifier: Optional[X12ID] = element(
        name="PAY18",
        description="Negative Amortization Qualifier",
    )

    Percent6: Optional[X12R] = element(
        name="PAY19",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount6: Optional[X12R] = element(
        name="PAY20",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    NegativeAmortizationCapSourceCode: Optional[X12ID] = element(
        name="PAY21",
        description="Negative Amortization Cap Source Code",
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="PAY22",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
