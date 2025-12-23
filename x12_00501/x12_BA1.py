# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BA1(Segment):
    """
    BA1 - Export Shipment Identifying Information
    
    Description:
        To transmit identifying data for an export shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BA1/
    """
    _id: Literal["BA1"] = id_element(name="BA1")

    RelatedCompanyIndicationCode: X12ID = element(
        name="BA101",
        description="Related Company Indication Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ActionCode: X12ID = element(
        name="BA102",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    TransportationMethodTypeCode: X12ID = element(
        name="BA103",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CountryCode: X12ID = element(
        name="BA104",
        description="Country Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="BA105",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    PostalCode: Optional[X12ID] = element(
        name="BA106",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    CountryCode2: Optional[X12ID] = element(
        name="BA107",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="BA108",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    Authority: Optional[X12AN] = element(
        name="BA109",
        description="Authority",
        min_length=1,
        max_length=20,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="BA110",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="BA111",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    VesselName: Optional[X12AN] = element(
        name="BA112",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )
