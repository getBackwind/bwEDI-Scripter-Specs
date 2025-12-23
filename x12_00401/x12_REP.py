# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class REP(Segment):
    """
    REP - Repair Action
    
    Description:
        To specify the action that was taken or is to be taken in response to a service request
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/REP/
    """
    _id: Literal["REP"] = id_element(name="REP")

    AssignedIdentification: Optional[X12AN] = element(
        name="REP01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="REP02",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="REP03",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="REP04",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="REP05",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="REP06",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="REP07",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    RepairActionCode: Optional[X12AN] = element(
        name="REP08",
        description="Repair Action Code",
        min_length=1,
        max_length=4,
    )

    Description: Optional[X12AN] = element(
        name="REP09",
        description="Description",
        min_length=1,
        max_length=80,
    )

    AgencyQualifierCode2: Optional[X12ID] = element(
        name="REP10",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier2: Optional[X12AN] = element(
        name="REP11",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    RepairComplexityCode: Optional[X12AN] = element(
        name="REP12",
        description="Repair Complexity Code",
        min_length=1,
        max_length=3,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="REP13",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="REP14",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    RepairActionCode2: Optional[X12AN] = element(
        name="REP15",
        description="Repair Action Code",
        min_length=1,
        max_length=4,
    )

    Description2: Optional[X12AN] = element(
        name="REP16",
        description="Description",
        min_length=1,
        max_length=80,
    )

    AgencyQualifierCode3: Optional[X12ID] = element(
        name="REP17",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier3: Optional[X12AN] = element(
        name="REP18",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="REP19",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    AuthorizationIdentification: Optional[X12AN] = element(
        name="REP20",
        description="Authorization Identification",
        min_length=1,
        max_length=4,
    )
