# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class EQ(Segment):
    """
    EQ - Eligibility or Benefit Inquiry
    
    Description:
        To specify inquired eligibility or benefit information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/EQ/
    """
    _id: Literal["EQ"] = id_element(name="EQ")

    ServiceTypeCode: Optional[X12ID] = element(
        name="EQ01",
        description="Service Type Code",
        min_length=1,
        max_length=2,
    )

    ProductServiceIDQualifier: X12ID = element(
        name="EQ0201",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="EQ0202",
        description="Product/Service ID",
        mandatory=True,
        min_length=0,
        max_length=48,
    )

    ProcedureModifier: Optional[X12AN] = element(
        name="EQ0203",
        description="Procedure Modifier",
        min_length=2,
        max_length=2,
    )

    ProcedureModifier2: Optional[X12AN] = element(
        name="EQ0204",
        description="Procedure Modifier",
        min_length=2,
        max_length=2,
    )

    ProcedureModifier3: Optional[X12AN] = element(
        name="EQ0205",
        description="Procedure Modifier",
        min_length=2,
        max_length=2,
    )

    ProcedureModifier4: Optional[X12AN] = element(
        name="EQ0206",
        description="Procedure Modifier",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="EQ0207",
        description="Description",
        min_length=1,
        max_length=80,
    )

    CoverageLevelCode: Optional[X12ID] = element(
        name="EQ03",
        description="Coverage Level Code",
        min_length=3,
        max_length=3,
    )

    InsuranceTypeCode: Optional[X12ID] = element(
        name="EQ04",
        description="Insurance Type Code",
        min_length=1,
        max_length=2,
    )
