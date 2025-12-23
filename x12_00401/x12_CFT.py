# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class CFT(Segment):
    """
    CFT - Cost Reporting Format Type
    
    Description:
        To identify the cost reporting type, type of units reported, and funds details for the Contract Funds Status Report (CFSR)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CFT/
    """
    _id: Literal["CFT"] = id_element(name="CFT")

    ReportTypeCode: X12ID = element(
        name="CFT01",
        description="Report Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ContractingFundingCode: Optional[X12ID] = element(
        name="CFT03",
        description="Contracting Funding Code",
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="CFT04",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="CFT05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    DateTimeQualifier2: Optional[X12ID] = element(
        name="CFT06",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="CFT07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AppropriationCode: Optional[X12ID] = element(
        name="CFT08",
        description="Appropriation Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="CFT09",
        description="Description",
        min_length=1,
        max_length=80,
    )
