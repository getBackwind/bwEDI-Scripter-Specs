# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class CM(Segment):
    """
    CM - Cargo Manifest
    
    Description:
        To identify specific flight or voyage information for multimodal shipments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CM/
    """
    _id: Literal["CM"] = id_element(name="CM")

    FlightVoyageNumber: Optional[X12AN] = element(
        name="CM01",
        description="Flight/Voyage Number",
        min_length=2,
        max_length=10,
    )

    PortOrTerminalFunctionCode: Optional[X12ID] = element(
        name="CM02",
        description="Port or Terminal Function Code",
        min_length=1,
        max_length=1,
    )

    PortName: Optional[X12AN] = element(
        name="CM03",
        description="Port Name",
        min_length=2,
        max_length=24,
    )

    Date: Optional[X12DT] = element(
        name="CM04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    BookingNumber: Optional[X12AN] = element(
        name="CM05",
        description="Booking Number",
        min_length=1,
        max_length=17,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="CM06",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="CM07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Date2: Optional[X12DT] = element(
        name="CM08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    VesselName: Optional[X12AN] = element(
        name="CM09",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )

    PierNumber: Optional[X12AN] = element(
        name="CM10",
        description="Pier Number",
        min_length=1,
        max_length=4,
    )

    PierName: Optional[X12AN] = element(
        name="CM11",
        description="Pier Name",
        min_length=2,
        max_length=14,
    )

    TerminalName: Optional[X12AN] = element(
        name="CM12",
        description="Terminal Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="CM13",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="CM14",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CM15",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    CorrectionIndicator: Optional[X12ID] = element(
        name="CM16",
        description="Correction Indicator",
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="CM17",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )
