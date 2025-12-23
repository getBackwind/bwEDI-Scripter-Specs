# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class BTC(Segment):
    """
    BTC - Beginning Segment for Parameter Trace Registration
    
    Description:
        To provide basic information regarding the parameter trace conditions described
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BTC/
    """
    _id: Literal["BTC"] = id_element(name="BTC")

    TransactionSetPurposeCode: X12ID = element(
        name="BTC01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ParameterTraceRegistrationTypeCode: X12ID = element(
        name="BTC02",
        description="Parameter Trace Registration Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ParameterTraceTypeCode: X12ID = element(
        name="BTC03",
        description="Parameter Trace Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    OutputEventSelectionCode: X12ID = element(
        name="BTC04",
        description="Output Event Selection Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: X12AN = element(
        name="BTC05",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="BTC06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="BTC07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="BTC08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Count: Optional[X12Nn] = element(
        name="BTC09",
        description="Count",
        min_length=1,
        max_length=9,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="BTC10",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    AssociationOfAmericanRailroadsAARPoolCode: Optional[X12ID] = element(
        name="BTC11",
        description="Association of American Railroads (AAR) Pool Code",
        min_length=7,
        max_length=7,
    )

    IndustryCode: Optional[X12AN] = element(
        name="BTC12",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
