# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class FA1(Segment):
    """
    FA1 - Type of Financial Accounting Data
    
    Description:
        To specify the organization controlling the content of the accounting citation, and the purpose associated with the accounting citation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FA1/
    """
    _id: Literal["FA1"] = id_element(name="FA1")

    AgencyQualifierCode: X12ID = element(
        name="FA101",
        description="Agency Qualifier Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ServicePromotionAllowanceOrChargeCode: Optional[X12ID] = element(
        name="FA102",
        description="Service, Promotion, Allowance, or Charge Code",
    )

    AllowanceOrChargeIndicator: Optional[X12ID] = element(
        name="FA103",
        description="Allowance or Charge Indicator",
    )
