# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class N10(Segment):
    """
    N10 - Quantity and Description
    
    Description:
        To indicate line item quantity, description, marks and numbers, commodity code, weight, and customs value
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/N10/
    """
    _id: Literal["N10"] = id_element(name="N10")

    Quantity: Optional[X12R] = element(
        name="N1001",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="N1002",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    MarksAndNumbers: Optional[X12AN] = element(
        name="N1003",
        description="Marks and Numbers",
        min_length=1,
        max_length=48,
    )

    CommodityCodeQualifier: Optional[X12ID] = element(
        name="N1004",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="N1005",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    CustomsShipmentValue: Optional[X12AN] = element(
        name="N1006",
        description="Customs Shipment Value",
        min_length=2,
        max_length=8,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="N1007",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="N1008",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="N1009",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ManifestUnitCode: Optional[X12ID] = element(
        name="N1010",
        description="Manifest Unit Code",
        min_length=1,
        max_length=3,
    )

    CountryCode: Optional[X12ID] = element(
        name="N1011",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    CountryCode2: Optional[X12ID] = element(
        name="N1012",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="N1013",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
