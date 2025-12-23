# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID


class RU3(Segment):
    """
    RU3 - Employing Carrier Claim Profile
    
    Description:
        To communicate employing carrier response to a sickness or unemployment claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RU3/
    """
    _id: Literal["RU3"] = id_element(name="RU3")

    Date: X12DT = element(
        name="RU301",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    PayrollStatusCode: Optional[X12ID] = element(
        name="RU302",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode: Optional[X12ID] = element(
        name="RU303",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode2: Optional[X12ID] = element(
        name="RU304",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode2: Optional[X12ID] = element(
        name="RU305",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode3: Optional[X12ID] = element(
        name="RU306",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode3: Optional[X12ID] = element(
        name="RU307",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode4: Optional[X12ID] = element(
        name="RU308",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode4: Optional[X12ID] = element(
        name="RU309",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode5: Optional[X12ID] = element(
        name="RU310",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode5: Optional[X12ID] = element(
        name="RU311",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode6: Optional[X12ID] = element(
        name="RU312",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode6: Optional[X12ID] = element(
        name="RU313",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode7: Optional[X12ID] = element(
        name="RU314",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode7: Optional[X12ID] = element(
        name="RU315",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode8: Optional[X12ID] = element(
        name="RU316",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode8: Optional[X12ID] = element(
        name="RU317",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode9: Optional[X12ID] = element(
        name="RU318",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode9: Optional[X12ID] = element(
        name="RU319",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode10: Optional[X12ID] = element(
        name="RU320",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode10: Optional[X12ID] = element(
        name="RU321",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode11: Optional[X12ID] = element(
        name="RU322",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode11: Optional[X12ID] = element(
        name="RU323",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode12: Optional[X12ID] = element(
        name="RU324",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode12: Optional[X12ID] = element(
        name="RU325",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode13: Optional[X12ID] = element(
        name="RU326",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode13: Optional[X12ID] = element(
        name="RU327",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )

    PayrollStatusCode14: Optional[X12ID] = element(
        name="RU328",
        description="Payroll Status Code",
        min_length=2,
        max_length=2,
    )

    WagesPaidCode14: Optional[X12ID] = element(
        name="RU329",
        description="Wages Paid Code",
        min_length=1,
        max_length=1,
    )
