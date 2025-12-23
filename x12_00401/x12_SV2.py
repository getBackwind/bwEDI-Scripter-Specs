# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SV2(Segment):
    """
    SV2 - Institutional Service
    
    Description:
        To specify the claim service detail for a Health Care institution
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SV2/
    """
    _id: Literal["SV2"] = id_element(name="SV2")

    ProductServiceID: Optional[X12AN] = element(
        name="SV201",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="SV203",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="SV204",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="SV205",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitRate: Optional[X12R] = element(
        name="SV206",
        description="Unit Rate",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="SV207",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SV208",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    NursingHomeResidentialStatusCode: Optional[X12ID] = element(
        name="SV209",
        description="Nursing Home Residential Status Code",
        min_length=1,
        max_length=1,
    )

    LevelOfCareCode: Optional[X12ID] = element(
        name="SV210",
        description="Level of Care Code",
        min_length=1,
        max_length=1,
    )
