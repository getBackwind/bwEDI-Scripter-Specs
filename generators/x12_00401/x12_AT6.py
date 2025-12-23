# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class AT6(Segment):
    """
    AT6 - International Manifest Information
    
    Description:
        To transmit international manifest data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AT6/
    """
    _id: Literal["AT6"] = id_element(name="AT6")

    InternationalDutiableStatusCode: X12ID = element(
        name="AT601",
        description="International Dutiable Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ImportExportCode: X12ID = element(
        name="AT602",
        description="Import/Export Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    TransportationTermsCode: Optional[X12ID] = element(
        name="AT603",
        description="Transportation Terms Code",
        min_length=3,
        max_length=3,
    )
