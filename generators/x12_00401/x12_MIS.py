# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MIS(Segment):
    """
    MIS - Mortgagee Information Status
    
    Description:
        To provide information indicating status in mortgagee name, address, or name and address
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MIS/
    """
    _id: Literal["MIS"] = id_element(name="MIS")

    MortgageeInformationStatusCode: X12ID = element(
        name="MIS01",
        description="Mortgagee Information Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="MIS02",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="MIS03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="MIS04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    JurisdictionCode: Optional[X12ID] = element(
        name="MIS05",
        description="Jurisdiction Code",
        min_length=3,
        max_length=3,
    )
