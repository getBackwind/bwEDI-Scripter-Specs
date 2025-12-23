# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class SWR(Segment):
    """
    SWR - Switching Rates
    
    Description:
        To transmit data relating to the rates for the switching service being performed.
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SWR/
    """
    _id: Literal["SWR"] = id_element(name="SWR")

    RateValueQualifier: X12ID = element(
        name="SWR01",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Rate: X12R = element(
        name="SWR02",
        description="Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    Rate2: X12R = element(
        name="SWR03",
        description="Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    AmountCharged: X12Nn = element(
        name="SWR04",
        description="Amount Charged",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    AmountQualifierCode: X12ID = element(
        name="SWR05",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    SpecialChargeOrAllowanceCode: X12ID = element(
        name="SWR06",
        description="Special Charge or Allowance Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )
