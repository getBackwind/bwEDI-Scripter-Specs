# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class ST(Segment):
    """
    ST - Transaction Set Header
    
    Description:
        To indicate the start of a transaction set and to assign a control number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ST/
    """
    _id: Literal["ST"] = id_element(name="ST")

    TransactionSetIdCode: X12ID = element(
        name="ST01",
        description="Transaction Set Identifier Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    TransactionSetID: X12AN = element(
        name="ST02",
        description="Transaction Set Control Number",
        mandatory=True,
        min_length=4,
        max_length=9,
    )

    ImplementationConventionPreference: Optional[X12AN] = element(
        name="ST03",
        description="Implementation Convention Preference",
        min_length=1,
        max_length=9,
    )
