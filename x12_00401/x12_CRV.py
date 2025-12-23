# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class CRV(Segment):
    """
    CRV - Product Origin Reference
    
    Description:
        To provide a means of transmitting product origin information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CRV/
    """
    _id: Literal["CRV"] = id_element(name="CRV")

    NetCostCode: Optional[X12ID] = element(
        name="CRV01",
        description="Net Cost Code",
        min_length=1,
        max_length=1,
    )

    Amount: Optional[X12Nn] = element(
        name="CRV02",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    CountryCode: Optional[X12ID] = element(
        name="CRV03",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    ProductProcessCharacteristicCode: Optional[X12ID] = element(
        name="CRV04",
        description="Product/Process Characteristic Code",
        min_length=2,
        max_length=3,
    )

    Percent: Optional[X12Nn] = element(
        name="CRV05",
        description="Percent",
        min_length=1,
        max_length=3,
    )

    CertificationClauseCode: Optional[X12ID] = element(
        name="CRV06",
        description="Certification/Clause Code",
        min_length=2,
        max_length=2,
    )

    PreferentialDutyCriteriaCode: Optional[X12ID] = element(
        name="CRV07",
        description="Preferential Duty Criteria Code",
        min_length=1,
        max_length=1,
    )
