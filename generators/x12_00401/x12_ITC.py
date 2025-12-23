# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class ITC(Segment):
    """
    ITC - Information Type and Comment Results
    
    Description:
        To specify the results of a general request for information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ITC/
    """
    _id: Literal["ITC"] = id_element(name="ITC")

    InformationRequestResultCode: X12ID = element(
        name="ITC01",
        description="Information Request Result Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    InformationType: Optional[X12ID] = element(
        name="ITC02",
        description="Information Type",
    )

    InformationStatusCode: Optional[X12ID] = element(
        name="ITC03",
        description="Information Status Code",
        min_length=1,
        max_length=1,
    )

    ActionCode: Optional[X12ID] = element(
        name="ITC04",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    FinancialInformationTypeCode: Optional[X12ID] = element(
        name="ITC05",
        description="Financial Information Type Code",
        min_length=1,
        max_length=1,
    )

    ConsolidationCode: Optional[X12ID] = element(
        name="ITC06",
        description="Consolidation Code",
        min_length=1,
        max_length=1,
    )

    ConditionIndicator: Optional[X12ID] = element(
        name="ITC07",
        description="Condition Indicator",
    )

    FinancialStatementFormatCode: Optional[X12ID] = element(
        name="ITC08",
        description="Financial Statement Format Code",
        min_length=1,
        max_length=1,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="ITC09",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="ITC10",
        description="Unit of Time Period or Interval",
    )

    Description: Optional[X12AN] = element(
        name="ITC11",
        description="Description",
        min_length=1,
        max_length=80,
    )

    SourceOfDisclosureCode: Optional[X12ID] = element(
        name="ITC12",
        description="Source of Disclosure Code",
        min_length=1,
        max_length=1,
    )
