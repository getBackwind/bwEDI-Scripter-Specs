# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PRR(Segment):
    """
    PRR - Problem Report
    
    Description:
        To describe a product condition causing an engineering change or the condition when presented for service, for a recall notice, or for a service bulletin
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PRR/
    """
    _id: Literal["PRR"] = id_element(name="PRR")

    AssignedIdentification: Optional[X12AN] = element(
        name="PRR01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="PRR02",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="PRR03",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    ComplaintCode: Optional[X12AN] = element(
        name="PRR04",
        description="Complaint Code",
        min_length=3,
        max_length=6,
    )

    Description: Optional[X12AN] = element(
        name="PRR05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    AgencyQualifierCode2: Optional[X12ID] = element(
        name="PRR06",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier2: Optional[X12AN] = element(
        name="PRR07",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    ServiceClassificationCode: Optional[X12AN] = element(
        name="PRR08",
        description="Service Classification Code",
        min_length=1,
        max_length=4,
    )

    AgencyQualifierCode3: Optional[X12ID] = element(
        name="PRR09",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier3: Optional[X12AN] = element(
        name="PRR10",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    SeverityConditionCode: Optional[X12AN] = element(
        name="PRR11",
        description="Severity Condition Code",
        min_length=1,
        max_length=2,
    )
