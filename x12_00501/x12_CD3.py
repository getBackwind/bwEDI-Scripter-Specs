# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class CD3(Segment):
    """
    CD3 - Carton (Package) Detail
    
    Description:
        To transmit identifying codes, weights, and other related information related to an individual carton (package)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CD3/
    """
    _id: Literal["CD3"] = id_element(name="CD3")

    WeightQualifier: Optional[X12ID] = element(
        name="CD301",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="CD302",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Zone: Optional[X12AN] = element(
        name="CD303",
        description="Zone",
        min_length=2,
        max_length=3,
    )

    ServiceStandard: Optional[X12Nn] = element(
        name="CD304",
        description="Service Standard",
        min_length=1,
        max_length=4,
    )

    ServiceLevelCode: Optional[X12ID] = element(
        name="CD305",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    PickupOrDeliveryCode: Optional[X12ID] = element(
        name="CD306",
        description="Pickup or Delivery Code",
        min_length=1,
        max_length=2,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="CD307",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    AmountCharged: Optional[X12Nn] = element(
        name="CD308",
        description="Amount Charged",
        min_length=1,
        max_length=15,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="CD309",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    AmountCharged2: Optional[X12Nn] = element(
        name="CD310",
        description="Amount Charged",
        min_length=1,
        max_length=15,
    )

    ServiceLevelCode2: Optional[X12ID] = element(
        name="CD311",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    ServiceLevelCode3: Optional[X12ID] = element(
        name="CD312",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="CD313",
        description="Payment Method Code",
        min_length=3,
        max_length=3,
    )

    CountryCode: Optional[X12ID] = element(
        name="CD314",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
