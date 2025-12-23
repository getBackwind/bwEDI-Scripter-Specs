# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class NCD(Segment):
    """
    NCD - Nonconformance Description
    
    Description:
        To describe the nonconformance condition
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/NCD/
    """
    _id: Literal["NCD"] = id_element(name="NCD")

    MeasurementAttributeCode: Optional[X12ID] = element(
        name="NCD01",
        description="Measurement Attribute Code",
        min_length=2,
        max_length=2,
    )

    NonconformanceDeterminationCode: Optional[X12ID] = element(
        name="NCD02",
        description="Nonconformance Determination Code",
        min_length=1,
        max_length=1,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="NCD03",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    ProductProcessCharacteristicCode: Optional[X12ID] = element(
        name="NCD04",
        description="Product/Process Characteristic Code",
        min_length=2,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="NCD05",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    ProductDescriptionCode: Optional[X12AN] = element(
        name="NCD06",
        description="Product Description Code",
        min_length=1,
        max_length=12,
    )

    Description: Optional[X12AN] = element(
        name="NCD07",
        description="Description",
        min_length=1,
        max_length=80,
    )
