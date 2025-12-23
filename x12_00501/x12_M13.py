# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class M13(Segment):
    """
    M13 - Manifest Amendment Details
    
    Description:
        To correct a manifest record prior to conveyance arrival or to amend a manifest record after conveyance arrival
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M13/
    """
    _id: Literal["M13"] = id_element(name="M13")

    StandardCarrierAlphaCode: X12ID = element(
        name="M1301",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    LocationIdentifier: X12AN = element(
        name="M1302",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    AmendmentTypeCode: Optional[X12ID] = element(
        name="M1303",
        description="Amendment Type Code",
        min_length=1,
        max_length=1,
    )

    BillOfLadingWaybillNumber: X12AN = element(
        name="M1304",
        description="Bill of Lading/Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=25,
    )

    Quantity: Optional[X12R] = element(
        name="M1305",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AmendmentCode: Optional[X12ID] = element(
        name="M1306",
        description="Amendment Code",
    )

    ActionCode: Optional[X12ID] = element(
        name="M1307",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    BillOfLadingWaybillNumber2: Optional[X12AN] = element(
        name="M1308",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=25,
    )

    StandardCarrierAlphaCode2: X12ID = element(
        name="M1309",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="M1310",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="M1311",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="M1312",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
