# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class GA(Segment):
    """
    GA - Canadian Grain Information
    
    Description:
        To transmit the transportation and distribution requirements of grain at Canadian ports
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/GA/
    """
    _id: Literal["GA"] = id_element(name="GA")

    FumigatedCleanedIndicator: Optional[X12ID] = element(
        name="GA01",
        description="Fumigated/Cleaned Indicator",
    )

    CommodityCode: Optional[X12AN] = element(
        name="GA02",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    InspectedWeighedIndicatorCode: Optional[X12ID] = element(
        name="GA03",
        description="Inspected/Weighed Indicator Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="GA04",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="GA05",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Week: Optional[X12Nn] = element(
        name="GA06",
        description="Week",
        min_length=6,
        max_length=6,
    )

    UnloadTerminalElevatorCode: Optional[X12ID] = element(
        name="GA07",
        description="Unload Terminal Elevator Code",
        min_length=3,
        max_length=4,
    )

    Date: Optional[X12DT] = element(
        name="GA08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Number: Optional[X12Nn] = element(
        name="GA09",
        description="Number",
        min_length=1,
        max_length=9,
    )

    MachineSeparableIndicatorCode: Optional[X12ID] = element(
        name="GA10",
        description="Machine Separable Indicator Code",
        min_length=2,
        max_length=2,
    )

    CanadianWheatBoardCWBMarketingClassCode: Optional[X12ID] = element(
        name="GA11",
        description="Canadian Wheat Board (CWB) Marketing Class Code",
        min_length=1,
        max_length=1,
    )

    CanadianWheatBoardCWBMarketingClassTypeCode: Optional[X12ID] = element(
        name="GA12",
        description="Canadian Wheat Board (CWB) Marketing Class Type Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="GA13",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="GA14",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="GA15",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    PercentQualifier: Optional[X12ID] = element(
        name="GA16",
        description="Percent Qualifier",
        min_length=1,
        max_length=2,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="GA17",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="GA18",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
