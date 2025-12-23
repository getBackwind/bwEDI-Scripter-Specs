# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class ZA(Segment):
    """
    ZA - Product Activity Reporting
    
    Description:
        To provide activity details concerning product being reported
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ZA/
    """
    _id: Literal["ZA"] = id_element(name="ZA")

    ActivityCode: X12ID = element(
        name="ZA01",
        description="Activity Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="ZA02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="ZA03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="ZA04",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="ZA05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="ZA06",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ZA07",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="ZA08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
