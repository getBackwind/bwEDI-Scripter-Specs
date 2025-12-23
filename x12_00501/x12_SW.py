# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class SW(Segment):
    """
    SW - Switching Charges
    
    Description:
        To transmit codes, descriptions, and values for switching performed
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SW/
    """
    _id: Literal["SW"] = id_element(name="SW")

    TariffApplicationCode: X12ID = element(
        name="SW01",
        description="Tariff Application Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ConditionSegmentLogicalConnector: X12AN = element(
        name="SW02",
        description="Condition Segment Logical Connector",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    ConditionCode: X12ID = element(
        name="SW03",
        description="Condition Code",
        mandatory=True,
        min_length=4,
        max_length=4,
    )

    ConditionValue: X12AN = element(
        name="SW04",
        description="Condition Value",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="SW05",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="SW06",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Rate: Optional[X12R] = element(
        name="SW07",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    Rule260JunctionCode: Optional[X12ID] = element(
        name="SW08",
        description="Rule 260 Junction Code",
        min_length=1,
        max_length=5,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="SW09",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )
