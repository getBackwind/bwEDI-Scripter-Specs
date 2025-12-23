# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class IRA(Segment):
    """
    IRA - Investor Reporting Action Code
    
    Description:
        To identify actions on or status of the mortgage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IRA/
    """
    _id: Literal["IRA"] = id_element(name="IRA")

    InvestorReportingActionCode: X12ID = element(
        name="IRA01",
        description="Investor Reporting Action Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="IRA02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="IRA03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )
