# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BFR(Segment):
    """
    BFR - Beginning Segment for Planning Schedule
    
    Description:
        To indicate the beginning of a planning schedule transaction set; whether a ship or delivery based forecast; and related forecast envelope dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BFR/
    """
    _id: Literal["BFR"] = id_element(name="BFR")

    TransactionSetPurposeCode: X12ID = element(
        name="BFR01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BFR02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="BFR03",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    ScheduleTypeQualifier: X12ID = element(
        name="BFR04",
        description="Schedule Type Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ScheduleQuantityQualifier: X12ID = element(
        name="BFR05",
        description="Schedule Quantity Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="BFR06",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="BFR07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date3: X12DT = element(
        name="BFR08",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date4: Optional[X12DT] = element(
        name="BFR09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ContractNumber: Optional[X12AN] = element(
        name="BFR10",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="BFR11",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    PlanningScheduleTypeCode: Optional[X12ID] = element(
        name="BFR12",
        description="Planning Schedule Type Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BFR13",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
