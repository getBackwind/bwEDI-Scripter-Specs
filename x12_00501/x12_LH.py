# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class LH(Segment):
    """
    LH - Mixed Hazardous Commodities
    
    Description:
        To specify hazardous line items in terms of hazardous mnemonic, identification number, reportable quantities, and limited quantities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LH/
    """
    _id: Literal["LH"] = id_element(name="LH")

    LadingLineItemNumber: X12Nn = element(
        name="LH01",
        description="Lading Line Item Number",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    HazardousMnemonicCode: X12ID = element(
        name="LH02",
        description="Hazardous Mnemonic Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="LH03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="LH04",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReportableQuantityCode: Optional[X12ID] = element(
        name="LH05",
        description="Reportable Quantity Code",
        min_length=2,
        max_length=2,
    )

    LimitedQuantityIndicationCode: Optional[X12ID] = element(
        name="LH06",
        description="Limited Quantity Indication Code",
        min_length=1,
        max_length=1,
    )
