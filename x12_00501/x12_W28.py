# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class W28(Segment):
    """
    W28 - Consolidation Information
    
    Description:
        To transmit freight consolidation information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W28/
    """
    _id: Literal["W28"] = id_element(name="W28")

    ConsolidationCode: X12ID = element(
        name="W2801",
        description="Consolidation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="W2802",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="W2803",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="W2804",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    TotalStopOffs: Optional[X12Nn] = element(
        name="W2805",
        description="Total Stop-offs",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="W2806",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="W2807",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    BillOfLadingWaybillNumber: Optional[X12AN] = element(
        name="W2808",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=25,
    )
