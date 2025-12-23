# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class HD(Segment):
    """
    HD - Health Coverage
    
    Description:
        To provide information on health coverage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/HD/
    """
    _id: Literal["HD"] = id_element(name="HD")

    MaintenanceTypeCode: X12ID = element(
        name="HD01",
        description="Maintenance Type Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    MaintenanceReasonCode: Optional[X12ID] = element(
        name="HD02",
        description="Maintenance Reason Code",
        min_length=2,
        max_length=2,
    )

    InsuranceLineCode: Optional[X12ID] = element(
        name="HD03",
        description="Insurance Line Code",
        min_length=2,
        max_length=3,
    )

    PlanCoverageDescription: Optional[X12AN] = element(
        name="HD04",
        description="Plan Coverage Description",
        min_length=1,
        max_length=50,
    )

    CoverageLevelCode: Optional[X12ID] = element(
        name="HD05",
        description="Coverage Level Code",
        min_length=3,
        max_length=3,
    )

    Count: Optional[X12Nn] = element(
        name="HD06",
        description="Count",
        min_length=1,
        max_length=9,
    )

    Count2: Optional[X12Nn] = element(
        name="HD07",
        description="Count",
        min_length=1,
        max_length=9,
    )

    UnderwritingDecisionCode: Optional[X12ID] = element(
        name="HD08",
        description="Underwriting Decision Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="HD09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    DrugHouseCode: Optional[X12ID] = element(
        name="HD10",
        description="Drug House Code",
        min_length=2,
        max_length=3,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="HD11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
