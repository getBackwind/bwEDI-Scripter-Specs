# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class SCH(Segment):
    """
    SCH - Line Item Schedule
    
    Description:
        To specify the data for scheduling a specific line-item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SCH/
    """
    _id: Literal["SCH"] = id_element(name="SCH")

    Quantity: X12R = element(
        name="SCH01",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="SCH02",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="SCH03",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    Name: Optional[X12AN] = element(
        name="SCH04",
        description="Name",
        min_length=1,
        max_length=60,
    )

    DateTimeQualifier: X12ID = element(
        name="SCH05",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Date: X12DT = element(
        name="SCH06",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="SCH07",
        description="Time",
        min_length=4,
        max_length=8,
    )

    DateTimeQualifier2: Optional[X12ID] = element(
        name="SCH08",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="SCH09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="SCH10",
        description="Time",
        min_length=4,
        max_length=8,
    )

    RequestReferenceNumber: Optional[X12AN] = element(
        name="SCH11",
        description="Request Reference Number",
        min_length=1,
        max_length=45,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="SCH12",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )
