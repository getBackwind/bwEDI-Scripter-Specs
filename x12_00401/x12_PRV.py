# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PRV(Segment):
    """
    PRV - Provider Information
    
    Description:
        To specify the identifying characteristics of a provider
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PRV/
    """
    _id: Literal["PRV"] = id_element(name="PRV")

    ProviderCode: X12ID = element(
        name="PRV01",
        description="Provider Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="PRV02",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="PRV03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="PRV04",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    ProviderOrganizationCode: Optional[X12ID] = element(
        name="PRV06",
        description="Provider Organization Code",
        min_length=3,
        max_length=3,
    )
