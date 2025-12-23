# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class M20(Segment):
    """
    M20 - Permit to Transfer Request Details
    
    Description:
        To provide Customs with Permit to Transfer details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M20/
    """
    _id: Literal["M20"] = id_element(name="M20")

    StandardCarrierAlphaCode: X12ID = element(
        name="M2001",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    BillOfLadingWaybillNumber: X12AN = element(
        name="M2002",
        description="Bill of Lading/Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=25,
    )

    EquipmentInitial: X12AN = element(
        name="M2003",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="M2004",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    LocationQualifier: X12ID = element(
        name="M2005",
        description="Location Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: X12AN = element(
        name="M2006",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="M2007",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="M2008",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="M2009",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )
