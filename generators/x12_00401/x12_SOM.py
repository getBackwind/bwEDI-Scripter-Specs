# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class SOM(Segment):
    """
    SOM - Status of Mortgage
    
    Description:
        To provide information on the status of a mortgage and the date actions were taken regarding the loan and the property
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SOM/
    """
    _id: Literal["SOM"] = id_element(name="SOM")

    LoanStatusCode: X12ID = element(
        name="SOM01",
        description="Loan Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="SOM02",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="SOM03",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SOM04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    TypeOfBankruptcyCode: Optional[X12ID] = element(
        name="SOM05",
        description="Type of Bankruptcy Code",
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="SOM06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SOM07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    LoanStatusCode2: Optional[X12ID] = element(
        name="SOM08",
        description="Loan Status Code",
        min_length=1,
        max_length=2,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="SOM09",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="SOM10",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    LoanStatusCode3: Optional[X12ID] = element(
        name="SOM11",
        description="Loan Status Code",
        min_length=1,
        max_length=2,
    )

    DateTimePeriodFormatQualifier3: Optional[X12ID] = element(
        name="SOM12",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="SOM13",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )
