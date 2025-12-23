# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class FBB(Segment):
    """
    FBB - Foreign and Industry Business
    
    Description:
        To specify amount or percentage of foreign and/or industry business by the trading partner
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FBB/
    """
    _id: Literal["FBB"] = id_element(name="FBB")

    CountryCode: X12ID = element(
        name="FBB01",
        description="Country Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="FBB02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="FBB03",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="FBB04",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="FBB05",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="FBB06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal2: Optional[X12R] = element(
        name="FBB07",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
