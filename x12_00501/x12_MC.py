# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class MC(Segment):
    """
    MC - Miscellaneous and Accessorial Charges
    
    Description:
        To transmit codes, descriptions, and values for miscellaneous or accessorial charges associated with rail rate data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MC/
    """
    _id: Literal["MC"] = id_element(name="MC")

    SpecialChargeOrAllowanceCode: X12ID = element(
        name="MC01",
        description="Special Charge or Allowance Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    RateValueQualifier: X12ID = element(
        name="MC02",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Rate: X12R = element(
        name="MC03",
        description="Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    SpecialChargeDescription: Optional[X12AN] = element(
        name="MC04",
        description="Special Charge Description",
        min_length=2,
        max_length=25,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="MC05",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )
