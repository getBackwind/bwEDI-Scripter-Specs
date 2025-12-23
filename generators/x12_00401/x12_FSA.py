# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class FSA(Segment):
    """
    FSA - Flexible Spending Account
    
    Description:
        To supply flexible spending account information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FSA/
    """
    _id: Literal["FSA"] = id_element(name="FSA")

    MaintenanceTypeCode: X12ID = element(
        name="FSA01",
        description="Maintenance Type Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    FlexibleSpendingAccountSelectionCode: Optional[X12ID] = element(
        name="FSA02",
        description="Flexible Spending Account Selection Code",
        min_length=1,
        max_length=1,
    )

    MaintenanceReasonCode: Optional[X12ID] = element(
        name="FSA03",
        description="Maintenance Reason Code",
        min_length=2,
        max_length=2,
    )

    AccountNumber: Optional[X12AN] = element(
        name="FSA04",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="FSA05",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    PlanCoverageDescription: Optional[X12AN] = element(
        name="FSA06",
        description="Plan Coverage Description",
        min_length=1,
        max_length=50,
    )

    ProductOptionCode: Optional[X12ID] = element(
        name="FSA07",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )

    ProductOptionCode2: Optional[X12ID] = element(
        name="FSA08",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )

    ProductOptionCode3: Optional[X12ID] = element(
        name="FSA09",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )
