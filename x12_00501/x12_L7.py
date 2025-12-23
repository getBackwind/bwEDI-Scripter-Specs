# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class L7(Segment):
    """
    L7 - Tariff Reference
    
    Description:
        To reference details of the tariff used to arrive at applicable rates or charge
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/L7/
    """
    _id: Literal["L7"] = id_element(name="L7")

    LadingLineItemNumber: Optional[X12Nn] = element(
        name="L701",
        description="Lading Line Item Number",
        min_length=1,
        max_length=3,
    )

    TariffAgencyCode: Optional[X12ID] = element(
        name="L702",
        description="Tariff Agency Code",
        min_length=1,
        max_length=4,
    )

    TariffNumber: Optional[X12AN] = element(
        name="L703",
        description="Tariff Number",
        min_length=1,
        max_length=7,
    )

    TariffSectionNumber: Optional[X12AN] = element(
        name="L704",
        description="Tariff Section Number",
        min_length=1,
        max_length=2,
    )

    TariffItemNumber: Optional[X12AN] = element(
        name="L705",
        description="Tariff Item Number",
        min_length=1,
        max_length=16,
    )

    TariffItemPart: Optional[X12Nn] = element(
        name="L706",
        description="Tariff Item Part",
        min_length=1,
        max_length=2,
    )

    FreightClassCode: Optional[X12AN] = element(
        name="L707",
        description="Freight Class Code",
        min_length=2,
        max_length=5,
    )

    TariffSupplementIdentifier: Optional[X12AN] = element(
        name="L708",
        description="Tariff Supplement Identifier",
        min_length=1,
        max_length=4,
    )

    ExParte: Optional[X12AN] = element(
        name="L709",
        description="Ex Parte",
        min_length=4,
        max_length=4,
    )

    Date: Optional[X12DT] = element(
        name="L710",
        description="Date",
        min_length=8,
        max_length=8,
    )

    RateBasisNumber: Optional[X12AN] = element(
        name="L711",
        description="Rate Basis Number",
        min_length=1,
        max_length=6,
    )

    TariffColumn: Optional[X12AN] = element(
        name="L712",
        description="Tariff Column",
        min_length=1,
        max_length=2,
    )

    TariffDistance: Optional[X12Nn] = element(
        name="L713",
        description="Tariff Distance",
        min_length=1,
        max_length=5,
    )

    DistanceQualifier: Optional[X12ID] = element(
        name="L714",
        description="Distance Qualifier",
        min_length=1,
        max_length=1,
    )

    CityName: Optional[X12AN] = element(
        name="L715",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="L716",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
