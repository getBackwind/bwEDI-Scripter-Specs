# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SSD(Segment):
    """
    SSD - Shipment Sort Segregate Data
    
    Description:
        To supply shipment sort segregate data and related shipment identification numbers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SSD/
    """
    _id: Literal["SSD"] = id_element(name="SSD")

    ReferenceIdentification: Optional[X12AN] = element(
        name="SSD01",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="SSD02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="SSD03",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    ApplicationErrorConditionCode: Optional[X12ID] = element(
        name="SSD04",
        description="Application Error Condition Code",
        min_length=1,
        max_length=3,
    )
