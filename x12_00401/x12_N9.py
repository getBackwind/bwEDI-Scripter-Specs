# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class N9(Segment):
    """
    N9 - Reference Identification
    
    Description:
        To transmit identifying information as specified by the Reference Identification Qualifier
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/N9/
    """
    _id: Literal["N9"] = id_element(name="N9")

    IdQualifier: X12ID = element(
        name="N901",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceID: Optional[X12AN] = element(
        name="N902",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="N903",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    Date: Optional[X12DT] = element(
        name="N904",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="N905",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="N906",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="N90701",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="N90702",
        description="Reference Identification",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="N90703",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="N90704",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier3: Optional[X12ID] = element(
        name="N90705",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="N90706",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
