# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CAT(Segment):
    """
    CAT - Category of Patient Information Service
    
    Description:
        To specify categories of patient information service
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CAT/
    """
    _id: Literal["CAT"] = id_element(name="CAT")

    ReportTypeCode: Optional[X12ID] = element(
        name="CAT01",
        description="Report Type Code",
        min_length=2,
        max_length=2,
    )

    ReportTransmissionCode: Optional[X12ID] = element(
        name="CAT02",
        description="Report Transmission Code",
        min_length=1,
        max_length=2,
    )

    VersionIdentifier: Optional[X12AN] = element(
        name="CAT03",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="CAT04",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="CAT05",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="CAT06",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    VersionIdentifier2: Optional[X12AN] = element(
        name="CAT07",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )
