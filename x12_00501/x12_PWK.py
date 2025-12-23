# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class PWK(Segment):
    """
    PWK - Paperwork
    
    Description:
        To identify the type or transmission or both of paperwork or supporting information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PWK/
    """
    _id: Literal["PWK"] = id_element(name="PWK")

    ReportTypeCode: X12ID = element(
        name="PWK01",
        description="Report Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReportTransmissionCode: Optional[X12ID] = element(
        name="PWK02",
        description="Report Transmission Code",
        min_length=1,
        max_length=2,
    )

    ReportCopiesNeeded: Optional[X12Nn] = element(
        name="PWK03",
        description="Report Copies Needed",
        min_length=1,
        max_length=2,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="PWK04",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="PWK05",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="PWK06",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Description: Optional[X12AN] = element(
        name="PWK07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    RequestCategoryCode: Optional[X12ID] = element(
        name="PWK09",
        description="Request Category Code",
        min_length=2,
        max_length=2,
    )
