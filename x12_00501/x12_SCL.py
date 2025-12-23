# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class SCL(Segment):
    """
    SCL - Rate Basis/Scales
    
    Description:
        To identify a scale or rate basis number associated with a particular geographic location or specific set of rates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SCL/
    """
    _id: Literal["SCL"] = id_element(name="SCL")

    RateBasisQualifier: X12ID = element(
        name="SCL01",
        description="Rate Basis Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RateBasisNumber: Optional[X12AN] = element(
        name="SCL02",
        description="Rate Basis Number",
        min_length=1,
        max_length=6,
    )

    RateBasisNumber2: Optional[X12AN] = element(
        name="SCL03",
        description="Rate Basis Number",
        min_length=1,
        max_length=6,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="SCL04",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="SCL05",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="SCL06",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="SCL07",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    TariffAddOnFactor: Optional[X12Nn] = element(
        name="SCL08",
        description="Tariff Add-On Factor",
        min_length=1,
        max_length=6,
    )

    TariffClassAdjustmentReference: Optional[X12AN] = element(
        name="SCL09",
        description="Tariff Class Adjustment Reference",
        min_length=1,
        max_length=6,
    )

    TariffClassAdjustmentReference2: Optional[X12AN] = element(
        name="SCL10",
        description="Tariff Class Adjustment Reference",
        min_length=1,
        max_length=6,
    )
