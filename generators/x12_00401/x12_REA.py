# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class REA(Segment):
    """
    REA - Real Estate Property Information
    
    Description:
        To provide a description of real estate or general property information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/REA/
    """
    _id: Literal["REA"] = id_element(name="REA")

    Quantity: Optional[X12R] = element(
        name="REA02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Date: Optional[X12DT] = element(
        name="REA03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PropertyOwnershipRightsCode: Optional[X12ID] = element(
        name="REA04",
        description="Property Ownership Rights Code",
        min_length=1,
        max_length=1,
    )

    Date2: Optional[X12DT] = element(
        name="REA05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StatusOfPlansForRealEstateAssetCode: Optional[X12ID] = element(
        name="REA06",
        description="Status of Plans for Real Estate Asset Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="REA07",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="REA08",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Quantity2: Optional[X12R] = element(
        name="REA10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="REA11",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="REA12",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    TypeOfResidenceCode: Optional[X12ID] = element(
        name="REA13",
        description="Type of Residence Code",
        min_length=1,
        max_length=1,
    )
