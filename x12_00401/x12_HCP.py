# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class HCP(Segment):
    """
    HCP - Health Care Pricing
    
    Description:
        To specify pricing or repricing information about a health care claim or line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/HCP/
    """
    _id: Literal["HCP"] = id_element(name="HCP")

    PricingMethodology: Optional[X12ID] = element(
        name="HCP01",
        description="Pricing Methodology",
    )

    MonetaryAmount: Optional[X12R] = element(
        name="HCP02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="HCP03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="HCP04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Rate: Optional[X12R] = element(
        name="HCP05",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="HCP06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="HCP07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="HCP08",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="HCP09",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="HCP10",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="HCP11",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="HCP12",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    RejectReasonCode: Optional[X12ID] = element(
        name="HCP13",
        description="Reject Reason Code",
        min_length=2,
        max_length=2,
    )

    PolicyComplianceCode: Optional[X12ID] = element(
        name="HCP14",
        description="Policy Compliance Code",
        min_length=1,
        max_length=1,
    )

    ExceptionCode: Optional[X12ID] = element(
        name="HCP15",
        description="Exception Code",
        min_length=1,
        max_length=1,
    )
