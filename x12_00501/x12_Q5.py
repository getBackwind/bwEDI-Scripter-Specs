# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class Q5(Segment):
    """
    Q5 - Status Details
    
    Description:
        To specify the status of the shipment in terms of dates, time, reference numbers, and location
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/Q5/
    """
    _id: Literal["Q5"] = id_element(name="Q5")

    ShipmentStatusCode: Optional[X12ID] = element(
        name="Q501",
        description="Shipment Status Code",
        min_length=1,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="Q502",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="Q503",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="Q504",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="Q505",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    CityName: Optional[X12AN] = element(
        name="Q506",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="Q507",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="Q508",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="Q509",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="Q510",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="Q511",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="Q512",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    DirectionIdentifierCode: Optional[X12ID] = element(
        name="Q513",
        description="Direction Identifier Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="Q514",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="Q515",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    DirectionIdentifierCode2: Optional[X12ID] = element(
        name="Q516",
        description="Direction Identifier Code",
        min_length=1,
        max_length=1,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="Q517",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    PickupOrDeliveryCode: Optional[X12ID] = element(
        name="Q518",
        description="Pickup or Delivery Code",
        min_length=1,
        max_length=2,
    )
