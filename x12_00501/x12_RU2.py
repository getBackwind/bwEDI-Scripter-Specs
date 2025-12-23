# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class RU2(Segment):
    """
    RU2 - Employing Carrier Response
    
    Description:
        To communicate information (from the employing carrier to the United States Railroad Retirement Board) pertinent to the processing of retirement claims
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RU2/
    """
    _id: Literal["RU2"] = id_element(name="RU2")

    RailRetirementActivityCode: X12ID = element(
        name="RU201",
        description="Rail Retirement Activity Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: X12AN = element(
        name="RU202",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: Optional[X12DT] = element(
        name="RU203",
        description="Date",
        min_length=8,
        max_length=8,
    )

    EmploymentStatusCode: Optional[X12ID] = element(
        name="RU204",
        description="Employment Status Code",
        min_length=2,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="RU205",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="RU206",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    Date2: Optional[X12DT] = element(
        name="RU207",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date3: Optional[X12DT] = element(
        name="RU208",
        description="Date",
        min_length=8,
        max_length=8,
    )
