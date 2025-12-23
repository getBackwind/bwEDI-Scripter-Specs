# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element


class IIS(Segment):
    """
    IIS - Interchange Identification Segment
    
    Description:
        To uniquely identify interchange control structures
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IIS/
    """
    _id: Literal["IIS"] = id_element(name="IIS")
