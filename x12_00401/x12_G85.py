# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class G85(Segment):
    """
    G85 - Record Integrity Check
    
    Description:
        To provide a secure method of identifying authenticity of record content
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G85/
    """
    _id: Literal["G85"] = id_element(name="G85")

    IntegrityCheckValue: X12AN = element(
        name="G8501",
        description="Integrity Check Value",
        mandatory=True,
        min_length=1,
        max_length=12,
    )
