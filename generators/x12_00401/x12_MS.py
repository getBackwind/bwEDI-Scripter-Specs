# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class MS(Segment):
    """
    MS - Miscellaneous Services
    
    Description:
        To transmit coded descriptions and changes for miscellaneous or special services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MS/
    """
    _id: Literal["MS"] = id_element(name="MS")

    AgencyQualifierCode: X12ID = element(
        name="MS01",
        description="Agency Qualifier Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    SpecialServicesCode: X12ID = element(
        name="MS02",
        description="Special Services Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    Charge: X12Nn = element(
        name="MS03",
        description="Charge",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="MS04",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Charge2: Optional[X12Nn] = element(
        name="MS05",
        description="Charge",
        min_length=1,
        max_length=12,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="MS06",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )
