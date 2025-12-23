# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class E01(Segment):
    """
    E01 - Electronic Form Main Heading
    
    Description:
        To provide the information related to all of the values for this instance of the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E01/
    """
    _id: Literal["E01"] = id_element(name="E01")

    MaintenanceOperationCode: X12ID = element(
        name="E0101",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ElectronicFormStandardsTypeCode: X12ID = element(
        name="E0102",
        description="Electronic Form Standards Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    VersionReleaseIndustryIdentifierCode: X12AN = element(
        name="E0103",
        description="Version / Release / Industry Identifier Code",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    FullOrPartialIndicator: X12ID = element(
        name="E0104",
        description="Full or Partial Indicator",
        mandatory=True,
    )
