# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class UD(Segment):
    """
    UD - Underwriting Status
    
    Description:
        To identify and describe underwriting status of submitted applications
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/UD/
    """
    _id: Literal["UD"] = id_element(name="UD")

    StatusCode: X12ID = element(
        name="UD01",
        description="Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StatusCode2: Optional[X12ID] = element(
        name="UD02",
        description="Status Code",
        min_length=2,
        max_length=2,
    )

    UnderwritingDecisionCode: Optional[X12ID] = element(
        name="UD03",
        description="Underwriting Decision Code",
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="UD04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Description: Optional[X12AN] = element(
        name="UD05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    OfferBasisCode: Optional[X12ID] = element(
        name="UD06",
        description="Offer Basis Code",
        min_length=2,
        max_length=2,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="UD07",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )

    OfferBasisCode2: Optional[X12ID] = element(
        name="UD08",
        description="Offer Basis Code",
        min_length=2,
        max_length=2,
    )

    AssignedNumber2: Optional[X12Nn] = element(
        name="UD09",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )

    Description2: Optional[X12AN] = element(
        name="UD10",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Percent: Optional[X12R] = element(
        name="UD11",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    Amount: Optional[X12Nn] = element(
        name="UD12",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Number: Optional[X12Nn] = element(
        name="UD13",
        description="Number",
        min_length=1,
        max_length=9,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="UD14",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="UD15",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="UD16",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode2: Optional[X12ID] = element(
        name="UD17",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
