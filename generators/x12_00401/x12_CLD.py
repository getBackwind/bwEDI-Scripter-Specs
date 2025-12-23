# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class CLD(Segment):
    """
    CLD - Load Detail
    
    Description:
        To specify the number of material loads shipped
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CLD/
    """
    _id: Literal["CLD"] = id_element(name="CLD")

    NumberOfLoads: X12Nn = element(
        name="CLD01",
        description="Number of Loads",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    NumberOfUnitsShipped: X12R = element(
        name="CLD02",
        description="Number of Units Shipped",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    PackagingCode: Optional[X12AN] = element(
        name="CLD03",
        description="Packaging Code",
        min_length=3,
        max_length=5,
    )

    Size: Optional[X12R] = element(
        name="CLD04",
        description="Size",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="CLD05",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
