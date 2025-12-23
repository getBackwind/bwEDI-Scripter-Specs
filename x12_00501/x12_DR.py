# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class DR(Segment):
    """
    DR - Docket Range
    
    Description:
        To assign an identification to a range of dockets
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DR/
    """
    _id: Literal["DR"] = id_element(name="DR")

    Date: X12DT = element(
        name="DR01",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="DR02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    DocketControlNumber: X12AN = element(
        name="DR03",
        description="Docket Control Number",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    DocketIdentification: X12AN = element(
        name="DR04",
        description="Docket Identification",
        mandatory=True,
        min_length=1,
        max_length=11,
    )

    RevisionNumber: Optional[X12Nn] = element(
        name="DR05",
        description="Revision Number",
        min_length=1,
        max_length=4,
    )

    DocketIdentification2: Optional[X12AN] = element(
        name="DR06",
        description="Docket Identification",
        min_length=1,
        max_length=11,
    )
