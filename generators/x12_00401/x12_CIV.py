# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CIV(Segment):
    """
    CIV - Civil Action Liability
    
    Description:
        To provide law suit, outstanding judgment, tax lien or foreclosure status
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CIV/
    """
    _id: Literal["CIV"] = id_element(name="CIV")

    PublicRecordOrObligationCode: X12ID = element(
        name="CIV01",
        description="Public Record or Obligation Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AmountQualifierCode: X12ID = element(
        name="CIV02",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="CIV03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="CIV04",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Name: Optional[X12AN] = element(
        name="CIV05",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Name2: Optional[X12AN] = element(
        name="CIV06",
        description="Name",
        min_length=1,
        max_length=60,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="CIV07",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CIV08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    CityName: Optional[X12AN] = element(
        name="CIV09",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    CountyDesignator: Optional[X12ID] = element(
        name="CIV10",
        description="County Designator",
        min_length=5,
        max_length=5,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="CIV11",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="CIV12",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="CIV13",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="CIV14",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="CIV15",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="CIV16",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Description: Optional[X12AN] = element(
        name="CIV17",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="CIV18",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
