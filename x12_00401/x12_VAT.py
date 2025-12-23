# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class VAT(Segment):
    """
    VAT - Vehicle Attribute
    
    Description:
        To Complete Performance Index (TCPI) for Budget at Complete (BAC)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/VAT/
    """
    _id: Literal["VAT"] = id_element(name="VAT")

    IndustryCode: Optional[X12AN] = element(
        name="VAT01",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="VAT02",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    Amount: Optional[X12Nn] = element(
        name="VAT03",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="VAT04",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    ProductProcessCharacteristicCode: Optional[X12ID] = element(
        name="VAT05",
        description="Product/Process Characteristic Code",
        min_length=2,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="VAT06",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="VAT07",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="VAT08",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="VAT09",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Quantity: Optional[X12R] = element(
        name="VAT10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="VAT11",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
