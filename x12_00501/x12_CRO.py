# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CRO(Segment):
    """
    CRO - Credit Report Order Details
    
    Description:
        To provide attributes of the credit report
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CRO/
    """
    _id: Literal["CRO"] = id_element(name="CRO")

    DateTimePeriodFormatQualifier: X12ID = element(
        name="CRO01",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="CRO02",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    ProductServiceIDQualifier: X12ID = element(
        name="CRO03",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="CRO04",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    ActionCode: X12ID = element(
        name="CRO05",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CreditReportMergeTypeCode: Optional[X12ID] = element(
        name="CRO06",
        description="Credit Report Merge Type Code",
        min_length=1,
        max_length=1,
    )
