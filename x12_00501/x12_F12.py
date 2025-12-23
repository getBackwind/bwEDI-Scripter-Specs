# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class F12(Segment):
    """
    F12 - Basic Claim Information - Automotive
    
    Description:
        To provide information for automotive claims
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/F12/
    """
    _id: Literal["F12"] = id_element(name="F12")

    ReferenceIdentification: X12AN = element(
        name="F1201",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: X12AN = element(
        name="F1202",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: X12DT = element(
        name="F1203",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    CreditDebitAdjustmentNumber: X12AN = element(
        name="F1204",
        description="Credit/Debit Adjustment Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    Date2: X12DT = element(
        name="F1205",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    LaborRate: X12Nn = element(
        name="F1206",
        description="Labor Rate",
        mandatory=True,
        min_length=3,
        max_length=6,
    )

    LaborRate2: X12Nn = element(
        name="F1207",
        description="Labor Rate",
        mandatory=True,
        min_length=3,
        max_length=6,
    )

    DamageCodeQualifier: Optional[X12ID] = element(
        name="F1208",
        description="Damage Code Qualifier",
        min_length=1,
        max_length=1,
    )
