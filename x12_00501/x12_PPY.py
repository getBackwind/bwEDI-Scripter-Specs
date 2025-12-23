# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PPY(Segment):
    """
    PPY - Personal Property Description
    
    Description:
        To provide details of personal property
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PPY/
    """
    _id: Literal["PPY"] = id_element(name="PPY")

    TypeOfPersonalOrBusinessAssetCode: X12ID = element(
        name="PPY01",
        description="Type of Personal or Business Asset Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: X12R = element(
        name="PPY02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Description: Optional[X12AN] = element(
        name="PPY03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description2: Optional[X12AN] = element(
        name="PPY04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description3: Optional[X12AN] = element(
        name="PPY05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="PPY06",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="PPY07",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PPY08",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
