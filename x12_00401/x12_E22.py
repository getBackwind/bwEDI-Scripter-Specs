# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class E22(Segment):
    """
    E22 - Data Element Relationships in a Segment
    
    Description:
        To provide the detail information for the data element relationships in a segment for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/E22/
    """
    _id: Literal["E22"] = id_element(name="E22")

    MaintenanceOperationCode: X12ID = element(
        name="E2201",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RelationCode: X12ID = element(
        name="E2202",
        description="Relation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PositionInSegment: X12Nn = element(
        name="E2203",
        description="Position in Segment",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    PositionInSegment2: Optional[X12Nn] = element(
        name="E2204",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )

    PositionInSegment3: Optional[X12Nn] = element(
        name="E2205",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )

    PositionInSegment4: Optional[X12Nn] = element(
        name="E2206",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )

    PositionInSegment5: Optional[X12Nn] = element(
        name="E2207",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )

    PositionInSegment6: Optional[X12Nn] = element(
        name="E2208",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )

    PositionInSegment7: Optional[X12Nn] = element(
        name="E2209",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )

    PositionInSegment8: Optional[X12Nn] = element(
        name="E2210",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )

    PositionInSegment9: Optional[X12Nn] = element(
        name="E2211",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )

    PositionInSegment10: Optional[X12Nn] = element(
        name="E2212",
        description="Position in Segment",
        min_length=1,
        max_length=2,
    )
