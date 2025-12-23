# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class AOI(Segment):
    """
    AOI - Animal Offspring/Fetus Identification
    
    Description:
        To identify offspring/fetuses of the parent animal
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AOI/
    """
    _id: Literal["AOI"] = id_element(name="AOI")

    YesNoConditionOrResponseCode: X12ID = element(
        name="AOI01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: X12AN = element(
        name="AOI02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    GenderCode: X12ID = element(
        name="AOI03",
        description="Gender Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    OffspringFetusStatusCode: Optional[X12ID] = element(
        name="AOI04",
        description="Offspring/Fetus Status Code",
        min_length=2,
        max_length=2,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="AOI05",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="AOI06",
        description="Unit of Time Period or Interval",
    )

    AnimalDispositionCode: Optional[X12ID] = element(
        name="AOI07",
        description="Animal Disposition Code",
        min_length=2,
        max_length=2,
    )

    TestPeriodOrIntervalValue2: Optional[X12Nn] = element(
        name="AOI08",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval2: Optional[X12ID] = element(
        name="AOI09",
        description="Unit of Time Period or Interval",
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="AOI10",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date: Optional[X12DT] = element(
        name="AOI11",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue3: Optional[X12Nn] = element(
        name="AOI12",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval3: Optional[X12ID] = element(
        name="AOI13",
        description="Unit of Time Period or Interval",
    )
