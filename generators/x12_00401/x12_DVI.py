# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DVI(Segment):
    """
    DVI - Dynamic Vehicle Information
    
    Description:
        To provide dynamic information pertaining to a vehicle
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DVI/
    """
    _id: Literal["DVI"] = id_element(name="DVI")

    PriceIdentifierCode: Optional[X12ID] = element(
        name="DVI01",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    UnitPrice: Optional[X12R] = element(
        name="DVI02",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="DVI03",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="DVI04",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="DVI05",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Name: Optional[X12AN] = element(
        name="DVI06",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Quantity: Optional[X12R] = element(
        name="DVI07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="DVI08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="DVI09",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="DVI10",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="DVI11",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    LicensePlateType: Optional[X12ID] = element(
        name="DVI12",
        description="License Plate Type",
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="DVI13",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
