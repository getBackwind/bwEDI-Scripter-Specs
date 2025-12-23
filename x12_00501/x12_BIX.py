# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BIX(Segment):
    """
    BIX - Beginning Segment for Automotive Inspection
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BIX/
    """
    _id: Literal["BIX"] = id_element(name="BIX")

    TransactionSetPurposeCode: X12ID = element(
        name="BIX01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="BIX02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Date: X12DT = element(
        name="BIX03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    InspectionLocationTypeCode: X12ID = element(
        name="BIX04",
        description="Inspection Location Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    RampIdentification: Optional[X12AN] = element(
        name="BIX05",
        description="Ramp Identification",
        min_length=1,
        max_length=9,
    )

    CityName: Optional[X12AN] = element(
        name="BIX06",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="BIX07",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    InspectorIdentityCode: Optional[X12AN] = element(
        name="BIX08",
        description="Inspector Identity Code",
        min_length=1,
        max_length=6,
    )

    DamageCodeQualifier: Optional[X12ID] = element(
        name="BIX09",
        description="Damage Code Qualifier",
        min_length=1,
        max_length=1,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="BIX10",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="BIX11",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
