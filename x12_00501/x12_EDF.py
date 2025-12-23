# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class EDF(Segment):
    """
    EDF - Educational Fee Information
    
    Description:
        To specify the type of educational fees assessed at an educational institution
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EDF/
    """
    _id: Literal["EDF"] = id_element(name="EDF")

    CodeListQualifierCode: X12ID = element(
        name="EDF01",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="EDF02",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    InstitutionalGovernanceOrFundingSourceLevelCode: Optional[X12ID] = element(
        name="EDF03",
        description="Institutional Governance or Funding Source Level Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode2: Optional[X12ID] = element(
        name="EDF04",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="EDF05",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="EDF06",
        description="Description",
        min_length=1,
        max_length=80,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="EDF07",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="EDF08",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity: Optional[X12R] = element(
        name="EDF09",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="EDF10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="EDF11",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
