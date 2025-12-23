# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class CTC(Segment):
    """
    CTC - Car Hire Transaction Control
    
    Description:
        To transmit identifying parties and document types
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CTC/
    """
    _id: Literal["CTC"] = id_element(name="CTC")

    StandardCarrierAlphaCode: X12ID = element(
        name="CTC01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: X12ID = element(
        name="CTC02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    CarHireDetailSummaryCode: X12ID = element(
        name="CTC03",
        description="Car Hire Detail/Summary Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AccountTypeCode: X12ID = element(
        name="CTC04",
        description="Account Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TransactionSetPurposeCode: X12ID = element(
        name="CTC05",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Year: X12Nn = element(
        name="CTC06",
        description="Year",
        mandatory=True,
        min_length=4,
        max_length=4,
    )

    MonthOfTheYearCode: X12ID = element(
        name="CTC07",
        description="Month of the Year Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Year2: Optional[X12Nn] = element(
        name="CTC08",
        description="Year",
        min_length=4,
        max_length=4,
    )

    MonthOfTheYearCode2: Optional[X12ID] = element(
        name="CTC09",
        description="Month of the Year Code",
        min_length=2,
        max_length=2,
    )

    AccountDescriptionCode: Optional[X12ID] = element(
        name="CTC10",
        description="Account Description Code",
        min_length=1,
        max_length=2,
    )
