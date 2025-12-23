# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class G19(Segment):
    """
    G19 - Line Item Detail - Quantity/Unit of Measure/Price Differences
    
    Description:
        To specify details when differences exist between 1) Quantities ordered/quantities shipped 2) Units of measurement 3) Pricing 4) Coupons redeemed/validated
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G19/
    """
    _id: Literal["G19"] = id_element(name="G19")

    NumberOfUnitsShipped: Optional[X12R] = element(
        name="G1901",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G1902",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    QuantityDifference: Optional[X12R] = element(
        name="G1903",
        description="Quantity Difference",
        min_length=1,
        max_length=9,
    )

    ShipmentOrderStatusCode: Optional[X12ID] = element(
        name="G1904",
        description="Shipment/Order Status Code",
        min_length=2,
        max_length=2,
    )

    PriceReasonCode: Optional[X12ID] = element(
        name="G1905",
        description="Price Reason Code",
        min_length=1,
        max_length=1,
    )

    TermsExceptionCode: Optional[X12ID] = element(
        name="G1906",
        description="Terms Exception Code",
        min_length=2,
        max_length=2,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="G1907",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G1908",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G1909",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
