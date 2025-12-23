# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class L4(Segment):
    """
    L4 - Measurement
    
    Description:
        To describe physical dimensions and quantities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/L4/
    """
    _id: Literal["L4"] = id_element(name="L4")

    Length: X12R = element(
        name="L401",
        description="Length",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    Width: X12R = element(
        name="L402",
        description="Width",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    Height: X12R = element(
        name="L403",
        description="Height",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    MeasurementUnitQualifier: X12ID = element(
        name="L404",
        description="Measurement Unit Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="L405",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IndustryCode: Optional[X12AN] = element(
        name="L406",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
