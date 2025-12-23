# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class SV5(Segment):
    """
    SV5 - Durable Medical Equipment Service
    
    Description:
        To specify the claim service detail for durable medical equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SV5/
    """
    _id: Literal["SV5"] = id_element(name="SV5")

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="SV502",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: X12R = element(
        name="SV503",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="SV504",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="SV505",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="SV506",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    PrognosisCode: Optional[X12ID] = element(
        name="SV507",
        description="Prognosis Code",
        min_length=1,
        max_length=1,
    )
