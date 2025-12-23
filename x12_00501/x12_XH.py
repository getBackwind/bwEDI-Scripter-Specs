# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class XH(Segment):
    """
    XH - Pro Forma - B13 Information
    
    Description:
        To specify a pro forma invoice and B13 Canada Customs Export Declaration information, required by U.S. and Canada Customs
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/XH/
    """
    _id: Literal["XH"] = id_element(name="XH")

    CurrencyCode: X12ID = element(
        name="XH01",
        description="Currency Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    RelatedCompanyIndicationCode: Optional[X12ID] = element(
        name="XH02",
        description="Related Company Indication Code",
        min_length=1,
        max_length=1,
    )

    SpecialChargeOrAllowanceCode: Optional[X12ID] = element(
        name="XH03",
        description="Special Charge or Allowance Code",
        min_length=3,
        max_length=3,
    )

    Amount: Optional[X12Nn] = element(
        name="XH04",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Block20Code: Optional[X12ID] = element(
        name="XH05",
        description="Block 20 Code",
        min_length=1,
        max_length=1,
    )

    ChemicalAnalysisPercentage: Optional[X12Nn] = element(
        name="XH06",
        description="Chemical Analysis Percentage",
        min_length=2,
        max_length=9,
    )

    UnitPrice: Optional[X12R] = element(
        name="XH07",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )
