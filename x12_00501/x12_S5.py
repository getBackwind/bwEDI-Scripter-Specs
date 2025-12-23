# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class S5(Segment):
    """
    S5 - Stop-off Details
    
    Description:
        To specify stop-off detail reference numbers and stop reason
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/S5/
    """
    _id: Literal["S5"] = id_element(name="S5")

    StopSequenceNumber: X12Nn = element(
        name="S501",
        description="Stop Sequence Number",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    StopReasonCode: X12ID = element(
        name="S502",
        description="Stop Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="S503",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="S504",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    NumberOfUnitsShipped: Optional[X12R] = element(
        name="S505",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="S506",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="S507",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="S508",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="S509",
        description="Description",
        min_length=1,
        max_length=80,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="S510",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    AccomplishCode: Optional[X12ID] = element(
        name="S511",
        description="Accomplish Code",
        min_length=1,
        max_length=1,
    )
