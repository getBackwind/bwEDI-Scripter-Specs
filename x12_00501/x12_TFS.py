# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class TFS(Segment):
    """
    TFS - Tax Form
    
    Description:
        To indicate the tax form or the type of tax form being reported
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TFS/
    """
    _id: Literal["TFS"] = id_element(name="TFS")

    ReferenceIdentificationQualifier: X12ID = element(
        name="TFS01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="TFS02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="TFS03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="TFS04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="TFS05",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="TFS06",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Date: Optional[X12DT] = element(
        name="TFS07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    NameControlIdentifier: Optional[X12AN] = element(
        name="TFS08",
        description="Name Control Identifier",
        min_length=1,
        max_length=4,
    )
