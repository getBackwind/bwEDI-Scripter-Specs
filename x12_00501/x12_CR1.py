# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CR1(Segment):
    """
    CR1 - Ambulance Certification
    
    Description:
        To supply information related to the ambulance service rendered to a patient
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CR1/
    """
    _id: Literal["CR1"] = id_element(name="CR1")

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="CR101",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="CR102",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    AmbulanceTransportCode: Optional[X12ID] = element(
        name="CR103",
        description="Ambulance Transport Code",
        min_length=1,
        max_length=1,
    )

    AmbulanceTransportReasonCode: Optional[X12ID] = element(
        name="CR104",
        description="Ambulance Transport Reason Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="CR105",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="CR106",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AddressInformation: Optional[X12AN] = element(
        name="CR107",
        description="Address Information",
        min_length=1,
        max_length=55,
    )

    AddressInformation2: Optional[X12AN] = element(
        name="CR108",
        description="Address Information",
        min_length=1,
        max_length=55,
    )

    Description: Optional[X12AN] = element(
        name="CR109",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description2: Optional[X12AN] = element(
        name="CR110",
        description="Description",
        min_length=1,
        max_length=80,
    )
