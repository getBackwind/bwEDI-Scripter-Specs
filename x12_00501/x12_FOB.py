# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class FOB(Segment):
    """
    FOB - F.O.B. Related Instructions
    
    Description:
        To specify transportation instructions relating to shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FOB/
    """
    _id: Literal["FOB"] = id_element(name="FOB")

    ShipmentPaymentMethod: X12ID = element(
        name="FOB01",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="FOB02",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="FOB03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    TransportationQualifier: Optional[X12ID] = element(
        name="FOB04",
        description="Transportation Terms Qualifier Code",
        min_length=2,
        max_length=2,
    )

    TransportationCode: Optional[X12ID] = element(
        name="FOB05",
        description="Transportation Terms Code",
        min_length=3,
        max_length=3,
    )

    LocationQualifier2: Optional[X12ID] = element(
        name="FOB06",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    Description2: Optional[X12AN] = element(
        name="FOB07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    RiskOfLossCode: Optional[X12ID] = element(
        name="FOB08",
        description="Risk of Loss Code",
        min_length=2,
        max_length=2,
    )

    Description3: Optional[X12AN] = element(
        name="FOB09",
        description="Description",
        min_length=1,
        max_length=80,
    )
