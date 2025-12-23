# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class L7A(Segment):
    """
    L7A - Contract Reference Identifier
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/L7A/
    """
    _id: Literal["L7A"] = id_element(name="L7A")

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="L7A01",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    RegulatoryAgencyCode: Optional[X12ID] = element(
        name="L7A02",
        description="Regulatory Agency Code",
        min_length=3,
        max_length=5,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="L7A03",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    IssuingCarrierIdentifier: Optional[X12AN] = element(
        name="L7A04",
        description="Issuing Carrier Identifier",
        min_length=1,
        max_length=10,
    )

    ContractNumber: Optional[X12AN] = element(
        name="L7A05",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    ContractSuffix: Optional[X12AN] = element(
        name="L7A06",
        description="Contract Suffix",
        min_length=1,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="L7A07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="L7A08",
        description="Date",
        min_length=8,
        max_length=8,
    )
