# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class RU1(Segment):
    """
    RU1 - Retirement Board Detail
    
    Description:
        To communicate information (from the United States Railroad Retirement Board to the employing carrier) pertinent to the processing of retirement claims
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RU1/
    """
    _id: Literal["RU1"] = id_element(name="RU1")

    RailRetirementActivityCode: X12ID = element(
        name="RU101",
        description="Rail Retirement Activity Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: X12AN = element(
        name="RU102",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Name: X12AN = element(
        name="RU103",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="RU104",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date: Optional[X12DT] = element(
        name="RU105",
        description="Date",
        min_length=8,
        max_length=8,
    )

    EmploymentCode: Optional[X12ID] = element(
        name="RU106",
        description="Employment Code",
        min_length=1,
        max_length=1,
    )

    UnemployedReasonCode: Optional[X12ID] = element(
        name="RU107",
        description="Unemployed Reason Code",
        min_length=1,
        max_length=1,
    )

    Date2: Optional[X12DT] = element(
        name="RU108",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ClaimProfile: Optional[X12AN] = element(
        name="RU109",
        description="Claim Profile",
        min_length=14,
        max_length=14,
    )
