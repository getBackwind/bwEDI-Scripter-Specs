# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class ETD(Segment):
    """
    ETD - Excess Transportation Detail
    
    Description:
        To specify information relating to premium transportation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ETD/
    """
    _id: Literal["ETD"] = id_element(name="ETD")

    ExcessTransportationReasonCode: X12ID = element(
        name="ETD01",
        description="Excess Transportation Reason Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ExcessTransportationResponsibilityCode: X12ID = element(
        name="ETD02",
        description="Excess Transportation Responsibility Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="ETD03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ETD04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReturnableContainerFreightPaymentResponsibilityCode: Optional[X12ID] = element(
        name="ETD05",
        description="Returnable Container Freight Payment Responsibility Code",
        min_length=1,
        max_length=1,
    )
