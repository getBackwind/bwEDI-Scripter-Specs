# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class API(Segment):
    """
    API - Activity or Process Information
    
    Description:
        To provide information on activity or process
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/API/
    """
    _id: Literal["API"] = id_element(name="API")

    CodeCategory: X12ID = element(
        name="API01",
        description="Code Category",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="API02",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    MaintenanceTypeCode: Optional[X12ID] = element(
        name="API03",
        description="Maintenance Type Code",
        min_length=3,
        max_length=3,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="API04",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    AffectedAreaOrSectionCode: Optional[X12ID] = element(
        name="API05",
        description="Affected Area or Section Code",
        min_length=1,
        max_length=1,
    )

    InsuranceTypeCode: Optional[X12ID] = element(
        name="API06",
        description="Insurance Type Code",
        min_length=1,
        max_length=2,
    )

    LoanTypeCode: Optional[X12ID] = element(
        name="API07",
        description="Loan Type Code",
        min_length=1,
        max_length=2,
    )

    InformationStatusCode: Optional[X12ID] = element(
        name="API08",
        description="Information Status Code",
        min_length=1,
        max_length=1,
    )
