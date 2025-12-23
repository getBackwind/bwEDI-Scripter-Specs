# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class E34(Segment):
    """
    E34 - Code List Values for a Data Element
    
    Description:
        To provide the code list values of a data element for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E34/
    """
    _id: Literal["E34"] = id_element(name="E34")

    MaintenanceOperationCode: X12ID = element(
        name="E3401",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CodeValue: X12AN = element(
        name="E3402",
        description="Code Value",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    PartitionIndicator: Optional[X12AN] = element(
        name="E3403",
        description="Partition Indicator",
        min_length=1,
        max_length=80,
    )

    Description: X12AN = element(
        name="E3404",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
