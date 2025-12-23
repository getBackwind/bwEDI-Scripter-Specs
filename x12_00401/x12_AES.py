# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class AES(Segment):
    """
    AES - Automatic Equipment Identification Site Information
    
    Description:
        To identify the status of an automatic equipment identification reader site
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AES/
    """
    _id: Literal["AES"] = id_element(name="AES")

    AutomaticEquipmentIdentificationSiteStatusCode: X12ID = element(
        name="AES01",
        description="Automatic Equipment Identification Site Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    MovementTypeCode: X12ID = element(
        name="AES02",
        description="Movement Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    TrainTerminationStatusCode: X12ID = element(
        name="AES03",
        description="Train Termination Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AutomaticEquipmentIdentificationConsistConfidenceLevelCode: X12ID = element(
        name="AES04",
        description="Automatic Equipment Identification Consist Confidence Level Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    IndustryCode: Optional[X12AN] = element(
        name="AES05",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
