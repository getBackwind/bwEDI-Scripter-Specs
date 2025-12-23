# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn


class MIN(Segment):
    """
    MIN - Minimum Detail
    
    Description:
        To indicate minimum units as defined in scale rate route
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MIN/
    """
    _id: Literal["MIN"] = id_element(name="MIN")

    LoadingRestriction: X12Nn = element(
        name="MIN01",
        description="Loading Restriction",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    LoadingRestriction2: Optional[X12Nn] = element(
        name="MIN02",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction3: Optional[X12Nn] = element(
        name="MIN03",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction4: Optional[X12Nn] = element(
        name="MIN04",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction5: Optional[X12Nn] = element(
        name="MIN05",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction6: Optional[X12Nn] = element(
        name="MIN06",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction7: Optional[X12Nn] = element(
        name="MIN07",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction8: Optional[X12Nn] = element(
        name="MIN08",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction9: Optional[X12Nn] = element(
        name="MIN09",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction10: Optional[X12Nn] = element(
        name="MIN10",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction11: Optional[X12Nn] = element(
        name="MIN11",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction12: Optional[X12Nn] = element(
        name="MIN12",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction13: Optional[X12Nn] = element(
        name="MIN13",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction14: Optional[X12Nn] = element(
        name="MIN14",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction15: Optional[X12Nn] = element(
        name="MIN15",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction16: Optional[X12Nn] = element(
        name="MIN16",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )
