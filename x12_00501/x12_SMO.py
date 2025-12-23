# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class SMO(Segment):
    """
    SMO - Operational Services
    
    Description:
        To identify the specific railroad operating facilities and characteristics for the station in the transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SMO/
    """
    _id: Literal["SMO"] = id_element(name="SMO")

    AutomobileRampFacilityCode: Optional[X12ID] = element(
        name="SMO01",
        description="Automobile Ramp Facility Code",
        min_length=1,
        max_length=1,
    )

    IntermodalFacilityCode: Optional[X12ID] = element(
        name="SMO02",
        description="Intermodal Facility Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SMO03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SMO04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="SMO05",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    RailCarPlateSizeCode: Optional[X12ID] = element(
        name="SMO06",
        description="Rail Car Plate Size Code",
        min_length=1,
        max_length=1,
    )

    ImportExportCode: Optional[X12ID] = element(
        name="SMO07",
        description="Import/Export Code",
        min_length=1,
        max_length=1,
    )
