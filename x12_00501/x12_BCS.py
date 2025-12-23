# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class BCS(Segment):
    """
    BCS - Beginning Segment for Project Cost Reporting
    
    Description:
        To indicate the beginning of the Project Cost Reporting Transaction Set and provide information identifying a program name, number, contract type, and security classification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BCS/
    """
    _id: Literal["BCS"] = id_element(name="BCS")

    TransactionSetPurposeCode: X12ID = element(
        name="BCS01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BCS02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ContractNumber: X12AN = element(
        name="BCS03",
        description="Contract Number",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date2: X12DT = element(
        name="BCS04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ContractTypeCode: Optional[X12ID] = element(
        name="BCS05",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="BCS06",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BCS07",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ProgramTypeCode: Optional[X12ID] = element(
        name="BCS08",
        description="Program Type Code",
        min_length=2,
        max_length=2,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BCS09",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="BCS10",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    PercentageAsDecimal2: Optional[X12R] = element(
        name="BCS11",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
