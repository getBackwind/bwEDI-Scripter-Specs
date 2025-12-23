# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class LH4(Segment):
    """
    LH4 - Canadian Dangerous Requirements
    
    Description:
        To specify additional Transport Canada requirements covering transportation of dangerous goods in Canada
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LH4/
    """
    _id: Literal["LH4"] = id_element(name="LH4")

    EmergencyResponsePlanNumber: Optional[X12AN] = element(
        name="LH401",
        description="Emergency Response Plan Number",
        min_length=1,
        max_length=12,
    )

    CommunicationNumber: Optional[X12AN] = element(
        name="LH402",
        description="Communication Number",
        min_length=1,
        max_length=80,
    )

    PackingGroupCode: Optional[X12ID] = element(
        name="LH403",
        description="Packing Group Code",
        min_length=1,
        max_length=3,
    )

    SubsidiaryClassification: Optional[X12ID] = element(
        name="LH404",
        description="Subsidiary Classification",
        min_length=1,
        max_length=3,
    )

    SubsidiaryClassification2: Optional[X12ID] = element(
        name="LH405",
        description="Subsidiary Classification",
        min_length=1,
        max_length=3,
    )

    SubsidiaryClassification3: Optional[X12ID] = element(
        name="LH406",
        description="Subsidiary Classification",
        min_length=1,
        max_length=3,
    )

    SubsidiaryRiskIndicator: Optional[X12ID] = element(
        name="LH407",
        description="Subsidiary Risk Indicator",
    )

    NetExplosiveQuantity: Optional[X12Nn] = element(
        name="LH408",
        description="Net Explosive Quantity",
        min_length=1,
        max_length=6,
    )

    CanadianHazardousNotation: Optional[X12AN] = element(
        name="LH409",
        description="Canadian Hazardous Notation",
        min_length=1,
        max_length=25,
    )

    SpecialCommodityIndicatorCode: Optional[X12ID] = element(
        name="LH410",
        description="Special Commodity Indicator Code",
        min_length=1,
        max_length=1,
    )

    CommunicationNumber2: Optional[X12AN] = element(
        name="LH411",
        description="Communication Number",
        min_length=1,
        max_length=80,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="LH412",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
