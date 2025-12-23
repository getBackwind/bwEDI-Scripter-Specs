# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class TCD(Segment):
    """
    TCD - Itemized Call Detail
    
    Description:
        To specify detail information for itemized calls
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TCD/
    """
    _id: Literal["TCD"] = id_element(name="TCD")

    AssignedIdentification: Optional[X12AN] = element(
        name="TCD01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Date: Optional[X12DT] = element(
        name="TCD02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="TCD03",
        description="Time",
        min_length=4,
        max_length=8,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="TCD04",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="TCD05",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="TCD06",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    LocationQualifier2: Optional[X12ID] = element(
        name="TCD07",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="TCD08",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="TCD09",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    MeasurementValue: Optional[X12R] = element(
        name="TCD10",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    MeasurementValue2: Optional[X12R] = element(
        name="TCD11",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="TCD12",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="TCD13",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="TCD14",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="TCD15",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    RelationshipCode: Optional[X12ID] = element(
        name="TCD16",
        description="Relationship Code",
        min_length=1,
        max_length=1,
    )
