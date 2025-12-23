# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class NA(Segment):
    """
    NA - Cross-Reference Equipment
    
    Description:
        To cross-reference additional equipment to a primary piece of equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/NA/
    """
    _id: Literal["NA"] = id_element(name="NA")

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="NA01",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="NA02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    EquipmentInitial: X12AN = element(
        name="NA03",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="NA04",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    CrossReferenceTypeCode: Optional[X12ID] = element(
        name="NA05",
        description="Cross Reference Type Code",
        min_length=1,
        max_length=1,
    )

    Position: Optional[X12AN] = element(
        name="NA06",
        description="Position",
        min_length=1,
        max_length=3,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="NA07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    EquipmentLength: Optional[X12Nn] = element(
        name="NA08",
        description="Equipment Length",
        min_length=4,
        max_length=5,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="NA09",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ChassisType: Optional[X12ID] = element(
        name="NA10",
        description="Chassis Type",
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="NA11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
