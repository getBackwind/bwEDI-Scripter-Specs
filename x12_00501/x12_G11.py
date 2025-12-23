# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G11(Segment):
    """
    G11 - Coupon Reporting Specifications
    
    Description:
        To specify coupon reporting requirements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G11/
    """
    _id: Literal["G11"] = id_element(name="G11")

    ReportingStructureIdentifier: X12AN = element(
        name="G1101",
        description="Reporting Structure Identifier",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    Category: X12AN = element(
        name="G1102",
        description="Category",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    Category2: Optional[X12AN] = element(
        name="G1103",
        description="Category",
        min_length=1,
        max_length=6,
    )

    Category3: Optional[X12AN] = element(
        name="G1104",
        description="Category",
        min_length=1,
        max_length=6,
    )

    Category4: Optional[X12AN] = element(
        name="G1105",
        description="Category",
        min_length=1,
        max_length=6,
    )

    Category5: Optional[X12AN] = element(
        name="G1106",
        description="Category",
        min_length=1,
        max_length=6,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="G1107",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="G1108",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="G1109",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="G1110",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )
