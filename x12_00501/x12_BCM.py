# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BCM(Segment):
    """
    BCM - Beginning Segment for Contractor Cost Data Reporting
    
    Description:
        To indicate the beginning of the contractor cost data reports and transmit identifying numbers, descriptions, action codes, program and contract type, funding identification, and security level
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BCM/
    """
    _id: Literal["BCM"] = id_element(name="BCM")

    TransactionSetPurposeCode: X12ID = element(
        name="BCM01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BCM02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: X12DT = element(
        name="BCM03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ContractNumber: Optional[X12AN] = element(
        name="BCM04",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="BCM05",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    ContractActionCode: Optional[X12ID] = element(
        name="BCM06",
        description="Contract Action Code",
        min_length=2,
        max_length=2,
    )

    ProgramTypeCode: Optional[X12ID] = element(
        name="BCM07",
        description="Program Type Code",
        min_length=2,
        max_length=2,
    )

    FreeFormDescription2: Optional[X12AN] = element(
        name="BCM08",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    ContractingFundingCode: Optional[X12ID] = element(
        name="BCM09",
        description="Contracting Funding Code",
        min_length=2,
        max_length=2,
    )

    ContractTypeCode: Optional[X12ID] = element(
        name="BCM10",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BCM11",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="BCM12",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
