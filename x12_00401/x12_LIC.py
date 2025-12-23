# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LIC(Segment):
    """
    LIC - License Information
    
    Description:
        To provide license information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LIC/
    """
    _id: Literal["LIC"] = id_element(name="LIC")

    StateOrProvinceCode: X12ID = element(
        name="LIC01",
        description="State or Province Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceIDQualifier: X12ID = element(
        name="LIC02",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="LIC03",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="LIC04",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    StatusCode: X12ID = element(
        name="LIC05",
        description="Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="LIC06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="LIC07",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="LIC08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
