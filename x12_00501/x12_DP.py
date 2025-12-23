# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class DP(Segment):
    """
    DP - Auto Claim Detail - Parts
    
    Description:
        To describe the parts involved in the repair of vehicle damage and to specify actions taken related to the parts
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DP/
    """
    _id: Literal["DP"] = id_element(name="DP")

    ActionCode: X12ID = element(
        name="DP01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="DP02",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Amount: Optional[X12Nn] = element(
        name="DP03",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount2: Optional[X12Nn] = element(
        name="DP04",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="DP05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ConditionIndicator: Optional[X12ID] = element(
        name="DP06",
        description="Condition Indicator",
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="DP07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="DP08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode4: Optional[X12ID] = element(
        name="DP09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode5: Optional[X12ID] = element(
        name="DP10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="DP11",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="DP12",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="DP13",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    PercentDecimalFormat: Optional[X12R] = element(
        name="DP14",
        description="Percent, Decimal Format",
        min_length=1,
        max_length=6,
    )

    AllowanceOrChargeTotalAmount: Optional[X12Nn] = element(
        name="DP15",
        description="Allowance or Charge Total Amount",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode6: Optional[X12ID] = element(
        name="DP16",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode7: Optional[X12ID] = element(
        name="DP17",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
