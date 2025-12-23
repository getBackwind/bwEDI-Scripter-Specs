# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class M21(Segment):
    """
    M21 - Supplementary In-Bond Information
    
    Description:
        To transmit data relating to a U.S. Customs in-bond movement
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M21/
    """
    _id: Literal["M21"] = id_element(name="M21")

    CustomsEntryTypeCode: X12ID = element(
        name="M2101",
        description="Customs Entry Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    LocationIdentifier: X12AN = element(
        name="M2102",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="M2103",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    BillOfLadingWaybillNumber: X12AN = element(
        name="M2104",
        description="Bill of Lading/Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=25,
    )

    MasterInBondTypeCode: Optional[X12ID] = element(
        name="M2105",
        description="Master In-bond Type Code",
        min_length=1,
        max_length=1,
    )

    InBondControlNumber: Optional[X12AN] = element(
        name="M2106",
        description="In-bond Control Number",
        min_length=1,
        max_length=25,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="M2107",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    BillOfLadingWaybillNumber2: Optional[X12AN] = element(
        name="M2108",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=25,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="M2109",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    BillOfLadingWaybillNumber3: Optional[X12AN] = element(
        name="M2110",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=25,
    )

    StandardCarrierAlphaCode4: Optional[X12ID] = element(
        name="M2111",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode5: Optional[X12ID] = element(
        name="M2112",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Quantity: Optional[X12R] = element(
        name="M2113",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="M2114",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="M2115",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
