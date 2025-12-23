# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class X4(Segment):
    """
    X4 - Customs Release Information
    
    Description:
        To identify items for release
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/X4/
    """
    _id: Literal["X4"] = id_element(name="X4")

    BillOfLadingWaybillNumber: Optional[X12AN] = element(
        name="X401",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=12,
    )

    Quantity: Optional[X12R] = element(
        name="X402",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    CustomsEntryTypeCode: Optional[X12ID] = element(
        name="X403",
        description="Customs Entry Type Code",
        min_length=2,
        max_length=2,
    )

    CustomsEntryNumber: Optional[X12AN] = element(
        name="X404",
        description="Customs Entry Number",
        min_length=1,
        max_length=15,
    )

    Date: X12DT = element(
        name="X405",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="X406",
        description="Time",
        min_length=4,
        max_length=8,
    )

    DispositionCode: X12ID = element(
        name="X407",
        description="Disposition Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    BillOfLadingWaybillNumber2: Optional[X12AN] = element(
        name="X408",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=12,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="X409",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="X410",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="X411",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="X412",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="X413",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="X414",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="X415",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="X416",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    TimeCode: Optional[X12ID] = element(
        name="X417",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
