# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class SS(Segment):
    """
    SS - Docket Control Status
    
    Description:
        To specify information about rate level and rate docket independence
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SS/
    """
    _id: Literal["SS"] = id_element(name="SS")

    Date: Optional[X12DT] = element(
        name="SS01",
        description="Date",
        min_length=8,
        max_length=8,
    )

    RateLevel: Optional[X12AN] = element(
        name="SS02",
        description="Rate Level",
        min_length=1,
        max_length=5,
    )

    RateDistributionCode: X12ID = element(
        name="SS03",
        description="Rate Distribution Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    IndependenceCode: Optional[X12ID] = element(
        name="SS04",
        description="Independence Code",
        min_length=1,
        max_length=1,
    )

    Date2: Optional[X12DT] = element(
        name="SS05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date3: Optional[X12DT] = element(
        name="SS06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    NumberOfPeriods: Optional[X12Nn] = element(
        name="SS07",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    Date4: Optional[X12DT] = element(
        name="SS08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    RateMaintenanceAuthorityCode: Optional[X12ID] = element(
        name="SS09",
        description="Rate Maintenance Authority Code",
        min_length=1,
        max_length=1,
    )
