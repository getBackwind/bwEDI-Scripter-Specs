# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class MCT(Segment):
    """
    MCT - Tariff Accessorial Charges
    
    Description:
        To identify accessorial charges and define the range for which each charge is applicable
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MCT/
    """
    _id: Literal["MCT"] = id_element(name="MCT")

    SpecialChargeOrAllowanceCode: X12ID = element(
        name="MCT01",
        description="Special Charge or Allowance Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    TariffValueCode: Optional[X12ID] = element(
        name="MCT02",
        description="Tariff Value Code",
        min_length=2,
        max_length=2,
    )

    RangeMinimum: Optional[X12R] = element(
        name="MCT03",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="MCT04",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="MCT05",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Rate: Optional[X12R] = element(
        name="MCT06",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    TariffReferenceFlag: Optional[X12ID] = element(
        name="MCT07",
        description="Tariff Reference Flag",
    )

    SpecialChargeDescription: Optional[X12AN] = element(
        name="MCT08",
        description="Special Charge Description",
        min_length=2,
        max_length=25,
    )
