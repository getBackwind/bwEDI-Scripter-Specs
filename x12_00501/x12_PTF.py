# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class PTF(Segment):
    """
    PTF - Property Transaction Financials
    
    Description:
        To provide the financial information related to a real estate transaction such as list price, sales price, rent, commissions, fees, sales taxes and closing costs
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PTF/
    """
    _id: Literal["PTF"] = id_element(name="PTF")

    AmountQualifierCode: X12ID = element(
        name="PTF01",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="PTF02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="PTF03",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="PTF05",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    TaxTypeCode: Optional[X12ID] = element(
        name="PTF06",
        description="Tax Type Code",
        min_length=2,
        max_length=2,
    )

    TaxExemptCode: Optional[X12ID] = element(
        name="PTF07",
        description="Tax Exempt Code",
        min_length=1,
        max_length=1,
    )
