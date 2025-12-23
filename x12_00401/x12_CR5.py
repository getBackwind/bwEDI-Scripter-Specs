# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CR5(Segment):
    """
    CR5 - Oxygen Therapy Certification
    
    Description:
        To supply information regarding certification of medical necessity for home oxygen therapy
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CR5/
    """
    _id: Literal["CR5"] = id_element(name="CR5")

    CertificationTypeCode: Optional[X12ID] = element(
        name="CR501",
        description="Certification Type Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="CR502",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    OxygenEquipmentTypeCode: Optional[X12ID] = element(
        name="CR503",
        description="Oxygen Equipment Type Code",
        min_length=1,
        max_length=1,
    )

    OxygenEquipmentTypeCode2: Optional[X12ID] = element(
        name="CR504",
        description="Oxygen Equipment Type Code",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="CR505",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Quantity2: Optional[X12R] = element(
        name="CR506",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="CR507",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity4: Optional[X12R] = element(
        name="CR508",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Description2: Optional[X12AN] = element(
        name="CR509",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Quantity5: Optional[X12R] = element(
        name="CR510",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity6: Optional[X12R] = element(
        name="CR511",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    OxygenTestConditionCode: Optional[X12ID] = element(
        name="CR512",
        description="Oxygen Test Condition Code",
        min_length=1,
        max_length=1,
    )

    OxygenTestFindingsCode: Optional[X12ID] = element(
        name="CR513",
        description="Oxygen Test Findings Code",
        min_length=1,
        max_length=1,
    )

    OxygenTestFindingsCode2: Optional[X12ID] = element(
        name="CR514",
        description="Oxygen Test Findings Code",
        min_length=1,
        max_length=1,
    )

    OxygenTestFindingsCode3: Optional[X12ID] = element(
        name="CR515",
        description="Oxygen Test Findings Code",
        min_length=1,
        max_length=1,
    )

    Quantity7: Optional[X12R] = element(
        name="CR516",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    OxygenDeliverySystemCode: Optional[X12ID] = element(
        name="CR517",
        description="Oxygen Delivery System Code",
        min_length=1,
        max_length=1,
    )

    OxygenEquipmentTypeCode3: Optional[X12ID] = element(
        name="CR518",
        description="Oxygen Equipment Type Code",
        min_length=1,
        max_length=1,
    )
