# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class VAD(Segment):
    """
    VAD - Vehicle Advice Detail
    
    Description:
        To provide detail for vehicle application edit results
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/VAD/
    """
    _id: Literal["VAD"] = id_element(name="VAD")

    VehicleIdentificationNumber: X12AN = element(
        name="VAD01",
        description="Vehicle Identification Number",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    InvoiceNumber: Optional[X12AN] = element(
        name="VAD02",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="VAD03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Rate: Optional[X12R] = element(
        name="VAD04",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    DealerCode: Optional[X12AN] = element(
        name="VAD05",
        description="Dealer Code",
        min_length=2,
        max_length=9,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="VAD06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ApplicationErrorConditionCode: Optional[X12ID] = element(
        name="VAD07",
        description="Application Error Condition Code",
        min_length=1,
        max_length=3,
    )

    ApplicationErrorConditionCode2: Optional[X12ID] = element(
        name="VAD08",
        description="Application Error Condition Code",
        min_length=1,
        max_length=3,
    )

    ApplicationErrorConditionCode3: Optional[X12ID] = element(
        name="VAD09",
        description="Application Error Condition Code",
        min_length=1,
        max_length=3,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="VAD10",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="VAD11",
        description="Date",
        min_length=8,
        max_length=8,
    )
