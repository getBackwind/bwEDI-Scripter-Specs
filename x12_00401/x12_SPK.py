# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SPK(Segment):
    """
    SPK - Specimen Kit Information
    
    Description:
        To identify and describe laboratory specimen kit information and handling requirements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SPK/
    """
    _id: Literal["SPK"] = id_element(name="SPK")

    SpecimenKitTypeCode: X12ID = element(
        name="SPK01",
        description="Specimen Kit Type Code",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="SPK02",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    Temperature: Optional[X12R] = element(
        name="SPK03",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="SPK04",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="SPK05",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
