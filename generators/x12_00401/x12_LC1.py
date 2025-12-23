# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class LC1(Segment):
    """
    LC1 - Lane Commitments
    
    Description:
        To specify the details concerning the lane covered by this proposal
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LC1/
    """
    _id: Literal["LC1"] = id_element(name="LC1")

    NumberOfShipments: Optional[X12Nn] = element(
        name="LC101",
        description="Number of Shipments",
        min_length=1,
        max_length=5,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="LC102",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Number: Optional[X12Nn] = element(
        name="LC103",
        description="Number",
        min_length=1,
        max_length=9,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="LC104",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="LC105",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    NumberOfShipments2: Optional[X12Nn] = element(
        name="LC106",
        description="Number of Shipments",
        min_length=1,
        max_length=5,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="LC107",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    LaneRanking: Optional[X12R] = element(
        name="LC108",
        description="Lane Ranking",
        min_length=1,
        max_length=4,
    )

    FreightRate: Optional[X12R] = element(
        name="LC109",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate2: Optional[X12R] = element(
        name="LC110",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="LC111",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="LC112",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
