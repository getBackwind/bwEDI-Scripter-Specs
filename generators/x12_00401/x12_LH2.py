# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class LH2(Segment):
    """
    LH2 - Hazardous Classification Information
    
    Description:
        To specify the hazardous notation and endorsement information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LH2/
    """
    _id: Literal["LH2"] = id_element(name="LH2")

    HazardousClassification: Optional[X12ID] = element(
        name="LH201",
        description="Hazardous Classification",
        min_length=1,
        max_length=30,
    )

    HazardousClassQualifier: Optional[X12ID] = element(
        name="LH202",
        description="Hazardous Class Qualifier",
        min_length=1,
        max_length=1,
    )

    HazardousPlacardNotation: Optional[X12ID] = element(
        name="LH203",
        description="Hazardous Placard Notation",
        min_length=14,
        max_length=40,
    )

    HazardousEndorsement: Optional[X12ID] = element(
        name="LH204",
        description="Hazardous Endorsement",
        min_length=4,
        max_length=25,
    )

    ReportableQuantityCode: Optional[X12ID] = element(
        name="LH205",
        description="Reportable Quantity Code",
        min_length=2,
        max_length=2,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="LH206",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Temperature: Optional[X12R] = element(
        name="LH207",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="LH208",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Temperature2: Optional[X12R] = element(
        name="LH209",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="LH210",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Temperature3: Optional[X12R] = element(
        name="LH211",
        description="Temperature",
        min_length=1,
        max_length=4,
    )
