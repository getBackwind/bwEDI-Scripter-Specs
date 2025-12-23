# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class M14(Segment):
    """
    M14 - General Order Status Information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M14/
    """
    _id: Literal["M14"] = id_element(name="M14")

    BillOfLadingWaybillNumber: X12AN = element(
        name="M1401",
        description="Bill of Lading/Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=25,
    )

    BillOfLadingStatusCode: X12ID = element(
        name="M1402",
        description="Bill of Lading Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CustomsEntryNumber: Optional[X12AN] = element(
        name="M1403",
        description="Customs Entry Number",
        min_length=1,
        max_length=15,
    )

    CustomsEntryTypeCode: Optional[X12ID] = element(
        name="M1404",
        description="Customs Entry Type Code",
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="M1405",
        description="Date",
        min_length=8,
        max_length=8,
    )

    BillOfLadingWaybillNumber2: Optional[X12AN] = element(
        name="M1406",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=25,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="M1407",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="M1408",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Quantity: X12R = element(
        name="M1409",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="M1410",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="M1411",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )
