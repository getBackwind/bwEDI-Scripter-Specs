# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LHE(Segment):
    """
    LHE - Empty Equipment Hazardous Material Information
    
    Description:
        To specify the "last contained" hazardous shipping name, placard notation, and reference numbers for empty equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LHE/
    """
    _id: Literal["LHE"] = id_element(name="LHE")

    HazardousMaterialShippingName: X12AN = element(
        name="LHE01",
        description="Hazardous Material Shipping Name",
        mandatory=True,
        min_length=1,
        max_length=25,
    )

    HazardousPlacardNotation: X12ID = element(
        name="LHE02",
        description="Hazardous Placard Notation",
        mandatory=True,
        min_length=14,
        max_length=40,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="LHE03",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="LHE04",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReportableQuantityCode: Optional[X12ID] = element(
        name="LHE05",
        description="Reportable Quantity Code",
        min_length=2,
        max_length=2,
    )
