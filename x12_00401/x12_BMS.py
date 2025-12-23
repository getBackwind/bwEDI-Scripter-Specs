# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BMS(Segment):
    """
    BMS - Beginning Segment For Material Safety Data Sheet
    
    Description:
        To indicate the beginning of the Material Safety Data Sheet Transaction Set, identify the distinct type of report, and transmit key identifying numbers and dates relating to that report
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BMS/
    """
    _id: Literal["BMS"] = id_element(name="BMS")

    TransactionSetPurposeCode: X12ID = element(
        name="BMS01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BMS02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    LanguageCode: Optional[X12ID] = element(
        name="BMS03",
        description="Language Code",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BMS04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    RevisionValue: Optional[X12AN] = element(
        name="BMS05",
        description="Revision Value",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BMS06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    RevisionValue2: Optional[X12AN] = element(
        name="BMS07",
        description="Revision Value",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="BMS08",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="BMS09",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
