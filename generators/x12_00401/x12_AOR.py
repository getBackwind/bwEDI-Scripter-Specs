# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class AOR(Segment):
    """
    AOR - Animal Observation Result
    
    Description:
        To report observation results at the specified location
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AOR/
    """
    _id: Literal["AOR"] = id_element(name="AOR")

    ObservationDistribution: Optional[X12AN] = element(
        name="AOR01",
        description="Observation Distribution",
        min_length=1,
        max_length=16,
    )

    ObservationSeverity: Optional[X12AN] = element(
        name="AOR02",
        description="Observation Severity",
        min_length=1,
        max_length=17,
    )

    NeoplasmCode: Optional[X12ID] = element(
        name="AOR03",
        description="Neoplasm Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="AOR04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    LinkageIdentifier: Optional[X12AN] = element(
        name="AOR05",
        description="Linkage Identifier",
        min_length=1,
        max_length=4,
    )

    LinkageIdentifier2: Optional[X12AN] = element(
        name="AOR06",
        description="Linkage Identifier",
        min_length=1,
        max_length=4,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="AOR07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="AOR08",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="AOR09",
        description="Unit of Time Period or Interval",
    )

    TestPeriodOrIntervalValue2: Optional[X12Nn] = element(
        name="AOR10",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval2: Optional[X12ID] = element(
        name="AOR11",
        description="Unit of Time Period or Interval",
    )

    TestPeriodOrIntervalValue3: Optional[X12Nn] = element(
        name="AOR12",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval3: Optional[X12ID] = element(
        name="AOR13",
        description="Unit of Time Period or Interval",
    )
