# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CON(Segment):
    """
    CON - Contract Number Detail
    
    Description:
        To specify contract or reference number and status
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CON/
    """
    _id: Literal["CON"] = id_element(name="CON")

    ReferenceIdentificationQualifier: X12ID = element(
        name="CON01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="CON02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ContractStatusCode: X12ID = element(
        name="CON03",
        description="Contract Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )
