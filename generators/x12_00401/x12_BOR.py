# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BOR(Segment):
    """
    BOR - Beginning of Report
    
    Description:
        To identify characteristic information of the report being transmitted
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BOR/
    """
    _id: Literal["BOR"] = id_element(name="BOR")

    ReportTypeCode: X12ID = element(
        name="BOR01",
        description="Report Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BOR02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BOR03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="BOR04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="BOR05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="BOR06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="BOR07",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BOR08",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="BOR09",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    LanguageCode: Optional[X12ID] = element(
        name="BOR10",
        description="Language Code",
        min_length=2,
        max_length=3,
    )
