# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MPI(Segment):
    """
    MPI - Military Personnel Information
    
    Description:
        To report military service data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MPI/
    """
    _id: Literal["MPI"] = id_element(name="MPI")

    InformationStatusCode: X12ID = element(
        name="MPI01",
        description="Information Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    EmploymentStatusCode: X12ID = element(
        name="MPI02",
        description="Employment Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    GovernmentServiceAffiliationCode: X12ID = element(
        name="MPI03",
        description="Government Service Affiliation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="MPI04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    MilitaryServiceRankCode: Optional[X12ID] = element(
        name="MPI05",
        description="Military Service Rank Code",
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="MPI06",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="MPI07",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )
