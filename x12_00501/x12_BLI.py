# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class BLI(Segment):
    """
    BLI - Basic Baseline Item Data
    
    Description:
        To specify basic item data: item identification, quantity, and price
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BLI/
    """
    _id: Literal["BLI"] = id_element(name="BLI")

    ProductServiceIDQualifier: X12ID = element(
        name="BLI01",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="BLI02",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    Quantity: Optional[X12R] = element(
        name="BLI03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="BLI04",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PriceIdentifierCode: Optional[X12ID] = element(
        name="BLI05",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    UnitPrice: Optional[X12R] = element(
        name="BLI06",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="BLI07",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="BLI08",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="BLI09",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="BLI10",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="BLI11",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier4: Optional[X12ID] = element(
        name="BLI12",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="BLI13",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductOptionCode: Optional[X12ID] = element(
        name="BLI14",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )

    ProductOptionCode2: Optional[X12ID] = element(
        name="BLI15",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )

    ProductOptionCode3: Optional[X12ID] = element(
        name="BLI16",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )

    ProductOptionCode4: Optional[X12ID] = element(
        name="BLI17",
        description="Product Option Code",
        min_length=1,
        max_length=2,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="BLI18",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )
