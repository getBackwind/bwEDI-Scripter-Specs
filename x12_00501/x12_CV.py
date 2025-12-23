# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class CV(Segment):
    """
    CV - Cycle/Summary Value
    
    Description:
        To identify the car hire value detail associated with a settlement
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CV/
    """
    _id: Literal["CV"] = id_element(name="CV")

    LoadEmptyStatusCode: X12ID = element(
        name="CV01",
        description="Load/Empty Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PaymentActionCode: Optional[X12ID] = element(
        name="CV02",
        description="Payment Action Code",
        min_length=2,
        max_length=2,
    )

    CarTypeGroupCode: Optional[X12ID] = element(
        name="CV03",
        description="Car Type Group Code",
        min_length=1,
        max_length=1,
    )

    TimePeriodUnitQualifier: Optional[X12ID] = element(
        name="CV04",
        description="Time Period Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="CV05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MileageSettlementCode: Optional[X12ID] = element(
        name="CV06",
        description="Mileage Settlement Code",
        min_length=1,
        max_length=1,
    )

    Quantity2: Optional[X12R] = element(
        name="CV07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="CV08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="CV09",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="CV10",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="CV11",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="CV12",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="CV13",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PenaltyCode: Optional[X12ID] = element(
        name="CV14",
        description="Penalty Code",
        min_length=1,
        max_length=1,
    )
