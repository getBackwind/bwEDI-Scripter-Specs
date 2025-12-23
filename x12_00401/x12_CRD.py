# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class CRD(Segment):
    """
    CRD - Content Reporting Detail
    
    Description:
        To supply the detail information necessary to fulfill mandated requirements for the reporting of non-domestic materials and/or components included in domestically produced products
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CRD/
    """
    _id: Literal["CRD"] = id_element(name="CRD")

    CountryCode: X12ID = element(
        name="CRD01",
        description="Country Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="CRD02",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="CRD03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12Nn] = element(
        name="CRD04",
        description="Percent",
        min_length=1,
        max_length=3,
    )
