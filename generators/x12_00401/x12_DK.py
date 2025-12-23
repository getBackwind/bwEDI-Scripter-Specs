# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class DK(Segment):
    """
    DK - Docket Header
    
    Description:
        To assign an identification to a docket
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DK/
    """
    _id: Literal["DK"] = id_element(name="DK")

    StandardCarrierAlphaCode: X12ID = element(
        name="DK01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    DocketControlNumber: X12AN = element(
        name="DK02",
        description="Docket Control Number",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    DocketIdentification: X12AN = element(
        name="DK03",
        description="Docket Identification",
        mandatory=True,
        min_length=1,
        max_length=11,
    )

    RevisionNumber: X12Nn = element(
        name="DK04",
        description="Revision Number",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    ConveyanceCode: Optional[X12ID] = element(
        name="DK05",
        description="Conveyance Code",
        min_length=1,
        max_length=1,
    )

    DocketTypeCode: Optional[X12ID] = element(
        name="DK06",
        description="Docket Type Code",
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="DK07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="DK08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ApplicationType: Optional[X12ID] = element(
        name="DK09",
        description="Application Type",
    )

    GroupTitle: Optional[X12AN] = element(
        name="DK10",
        description="Group Title",
        min_length=2,
        max_length=30,
    )
