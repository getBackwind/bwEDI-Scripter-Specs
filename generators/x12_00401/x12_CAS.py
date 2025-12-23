# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class CAS(Segment):
    """
    CAS - Claims Adjustment
    
    Description:
        To supply adjustment reason codes and amounts as needed for an entire claim or for a particular service within the claim being paid
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CAS/
    """
    _id: Literal["CAS"] = id_element(name="CAS")

    ClaimAdjustmentGroupCode: X12ID = element(
        name="CAS01",
        description="Claim Adjustment Group Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ClaimAdjustmentReasonCode: X12ID = element(
        name="CAS02",
        description="Claim Adjustment Reason Code",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    MonetaryAmount: X12R = element(
        name="CAS03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="CAS04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ClaimAdjustmentReasonCode2: Optional[X12ID] = element(
        name="CAS05",
        description="Claim Adjustment Reason Code",
        min_length=1,
        max_length=5,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="CAS06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity2: Optional[X12R] = element(
        name="CAS07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ClaimAdjustmentReasonCode3: Optional[X12ID] = element(
        name="CAS08",
        description="Claim Adjustment Reason Code",
        min_length=1,
        max_length=5,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="CAS09",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity3: Optional[X12R] = element(
        name="CAS10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ClaimAdjustmentReasonCode4: Optional[X12ID] = element(
        name="CAS11",
        description="Claim Adjustment Reason Code",
        min_length=1,
        max_length=5,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="CAS12",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity4: Optional[X12R] = element(
        name="CAS13",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ClaimAdjustmentReasonCode5: Optional[X12ID] = element(
        name="CAS14",
        description="Claim Adjustment Reason Code",
        min_length=1,
        max_length=5,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="CAS15",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity5: Optional[X12R] = element(
        name="CAS16",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ClaimAdjustmentReasonCode6: Optional[X12ID] = element(
        name="CAS17",
        description="Claim Adjustment Reason Code",
        min_length=1,
        max_length=5,
    )

    MonetaryAmount6: Optional[X12R] = element(
        name="CAS18",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity6: Optional[X12R] = element(
        name="CAS19",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
