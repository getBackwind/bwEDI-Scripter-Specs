# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class BSW(Segment):
    """
    BSW - Beginning Segment for Carrier's Services Settlement
    
    Description:
        To transmit basic data relating to the carrierï¿½s settlement.
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BSW/
    """
    _id: Literal["BSW"] = id_element(name="BSW")

    Date: X12DT = element(
        name="BSW01",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="BSW02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: X12ID = element(
        name="BSW03",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    NetAmountDue: X12Nn = element(
        name="BSW04",
        description="Net Amount Due",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    BillingCode: X12ID = element(
        name="BSW05",
        description="Billing Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CorrectionIndicator: Optional[X12ID] = element(
        name="BSW06",
        description="Correction Indicator",
    )

    StatementNumber: Optional[X12AN] = element(
        name="BSW07",
        description="Statement Number",
        min_length=1,
        max_length=16,
    )
