# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class DRT(Segment):
    """
    DRT - Deprescription Rate Detail
    
    Description:
        To identify the deprescribed rate and type
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DRT/
    """
    _id: Literal["DRT"] = id_element(name="DRT")

    LoadEmptyStatusCode: Optional[X12ID] = element(
        name="DRT01",
        description="Load/Empty Status Code",
        min_length=1,
        max_length=1,
    )

    BilledRatedAsQualifier: Optional[X12ID] = element(
        name="DRT02",
        description="Billed/Rated-as Qualifier",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="DRT03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12R] = element(
        name="DRT04",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    ChangeTypeCode: Optional[X12ID] = element(
        name="DRT05",
        description="Change Type Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="DRT06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
