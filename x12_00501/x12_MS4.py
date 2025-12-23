# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class MS4(Segment):
    """
    MS4 - Shipment or Package Dimensions
    
    Description:
        To identify the dimensions of a shipment or package
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MS4/
    """
    _id: Literal["MS4"] = id_element(name="MS4")

    MeasurementUnitQualifier: X12ID = element(
        name="MS401",
        description="Measurement Unit Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Length: X12R = element(
        name="MS402",
        description="Length",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    Height: X12R = element(
        name="MS403",
        description="Height",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    Width: X12R = element(
        name="MS404",
        description="Width",
        mandatory=True,
        min_length=1,
        max_length=8,
    )
