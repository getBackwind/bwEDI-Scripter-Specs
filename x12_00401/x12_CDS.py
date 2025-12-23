# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CDS(Segment):
    """
    CDS - Case Description
    
    Description:
        To identify and describe a specific court case
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CDS/
    """
    _id: Literal["CDS"] = id_element(name="CDS")

    CaseTypeCode: X12ID = element(
        name="CDS01",
        description="Case Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    AdministrationOfJusticeOrganizationTypeCode: X12ID = element(
        name="CDS02",
        description="Administration of Justice Organization Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="CDS03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CDS04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="CDS05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="CDS06",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="CDS07",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="CDS08",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="CDS09",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier3: Optional[X12ID] = element(
        name="CDS10",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode3: Optional[X12AN] = element(
        name="CDS11",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
