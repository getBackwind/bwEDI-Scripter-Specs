# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class R12(Segment):
    """
    R12 - Work Order Information
    
    Description:
        To provide summary information for work order details for a specific piece of equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R12/
    """
    _id: Literal["R12"] = id_element(name="R12")

    NumberOfLineItems: X12Nn = element(
        name="R1201",
        description="Number of Line Items",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    EquipmentInitial: X12AN = element(
        name="R1202",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="R1203",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    ReferenceIdentification: X12AN = element(
        name="R1204",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: X12DT = element(
        name="R1205",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="R1206",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LoadEmptyStatusCode: Optional[X12ID] = element(
        name="R1207",
        description="Load/Empty Status Code",
        min_length=1,
        max_length=1,
    )

    EquipmentInitial2: Optional[X12AN] = element(
        name="R1208",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber2: Optional[X12AN] = element(
        name="R1209",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    EquipmentNumberCheckDigit: Optional[X12Nn] = element(
        name="R1210",
        description="Equipment Number Check Digit",
        min_length=1,
        max_length=1,
    )
