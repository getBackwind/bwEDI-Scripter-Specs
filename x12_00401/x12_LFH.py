# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LFH(Segment):
    """
    LFH - Freeform Hazardous Material Information
    
    Description:
        To uniquely identify the variable information required by government regulation covering the transportation of hazardous material shipments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LFH/
    """
    _id: Literal["LFH"] = id_element(name="LFH")

    HazardousMaterialShipmentInformationQualifier: X12ID = element(
        name="LFH01",
        description="Hazardous Material Shipment Information Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    HazardousMaterialShipmentInformation: X12AN = element(
        name="LFH02",
        description="Hazardous Material Shipment Information",
        mandatory=True,
        min_length=1,
        max_length=25,
    )

    HazardousMaterialShipmentInformation2: Optional[X12AN] = element(
        name="LFH03",
        description="Hazardous Material Shipment Information",
        min_length=1,
        max_length=25,
    )

    HazardZoneCode: Optional[X12ID] = element(
        name="LFH04",
        description="Hazard Zone Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="LFH05",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="LFH06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="LFH07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
