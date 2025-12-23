# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class Q8(Segment):
    """
    Q8 - Detail Delivery Exception Information
    
    Description:
        To transmit detailed lading data, damage, and disposition information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/Q8/
    """
    _id: Literal["Q8"] = id_element(name="Q8")

    LadingExceptionCode: X12ID = element(
        name="Q801",
        description="Lading Exception Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PackagingFormCode: Optional[X12ID] = element(
        name="Q802",
        description="Packaging Form Code",
        min_length=3,
        max_length=3,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="Q803",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="Q804",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="Q805",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    LadingDescription: Optional[X12AN] = element(
        name="Q806",
        description="Lading Description",
        min_length=1,
        max_length=50,
    )

    DamageReasonCode: Optional[X12ID] = element(
        name="Q807",
        description="Damage Reason Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="Q808",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="Q809",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="Q810",
        description="Description",
        min_length=1,
        max_length=80,
    )
