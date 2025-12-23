# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DSB(Segment):
    """
    DSB - Disability Information
    
    Description:
        To supply disability information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DSB/
    """
    _id: Literal["DSB"] = id_element(name="DSB")

    DisabilityTypeCode: X12ID = element(
        name="DSB01",
        description="Disability Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="DSB02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    OccupationCode: Optional[X12ID] = element(
        name="DSB03",
        description="Occupation Code",
        min_length=4,
        max_length=6,
    )

    WorkIntensityCode: Optional[X12ID] = element(
        name="DSB04",
        description="Work Intensity Code",
        min_length=1,
        max_length=1,
    )

    ProductOptionCode: Optional[X12ID] = element(
        name="DSB05",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="DSB06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="DSB07",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    MedicalCodeValue: Optional[X12AN] = element(
        name="DSB08",
        description="Medical Code Value",
        min_length=1,
        max_length=15,
    )
