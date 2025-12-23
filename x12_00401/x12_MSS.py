# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MSS(Segment):
    """
    MSS - Material Safety Data Sheet Section Information
    
    Description:
        To identify the report section
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MSS/
    """
    _id: Literal["MSS"] = id_element(name="MSS")

    ReportSectionNameCode: Optional[X12ID] = element(
        name="MSS01",
        description="Report Section Name Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="MSS02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="MSS03",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="MSS04",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    ChangeTypeCode: Optional[X12ID] = element(
        name="MSS05",
        description="Change Type Code",
        min_length=1,
        max_length=1,
    )

    ReportSectionNumber: Optional[X12AN] = element(
        name="MSS06",
        description="Report Section Number",
        min_length=1,
        max_length=15,
    )

    SafetyCharacteristicHazardCode: Optional[X12ID] = element(
        name="MSS07",
        description="Safety Characteristic/Hazard Code",
        min_length=3,
        max_length=3,
    )
