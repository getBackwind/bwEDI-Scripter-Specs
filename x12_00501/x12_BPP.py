# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BPP(Segment):
    """
    BPP - Beginning Segment for Project Schedule Reporting
    
    Description:
        To indicate the beginning of the Project Schedule Reporting Transaction Set and program identifying numbers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BPP/
    """
    _id: Literal["BPP"] = id_element(name="BPP")

    TransactionSetPurposeCode: X12ID = element(
        name="BPP01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BPP02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    NetworkOrScheduleDataType: X12ID = element(
        name="BPP03",
        description="Network or Schedule Data Type",
        mandatory=True,
    )

    ContractNumber: Optional[X12AN] = element(
        name="BPP04",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="BPP05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BPP06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date2: Optional[X12DT] = element(
        name="BPP07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReportTypeCode: Optional[X12ID] = element(
        name="BPP08",
        description="Report Type Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BPP09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Description2: Optional[X12AN] = element(
        name="BPP10",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Date3: Optional[X12DT] = element(
        name="BPP11",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="BPP12",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BPP13",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    VersionIdentifier: Optional[X12AN] = element(
        name="BPP14",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )
