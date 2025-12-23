# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class F6X(Segment):
    """
    F6X - Identification (Automotive)
    
    Description:
        To identify automotive vehicles in a loss or damage claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/F6X/
    """
    _id: Literal["F6X"] = id_element(name="F6X")

    VehicleIdentificationNumber: X12AN = element(
        name="F6X01",
        description="Vehicle Identification Number",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    AutomotiveManufacturersCode: X12ID = element(
        name="F6X02",
        description="Automotive Manufacturers Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DealerCode: X12AN = element(
        name="F6X03",
        description="Dealer Code",
        mandatory=True,
        min_length=2,
        max_length=9,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="F6X04",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="F6X05",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    InvoiceNumber: X12AN = element(
        name="F6X06",
        description="Invoice Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    Date: Optional[X12DT] = element(
        name="F6X07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="F6X08",
        description="Date",
        min_length=8,
        max_length=8,
    )
