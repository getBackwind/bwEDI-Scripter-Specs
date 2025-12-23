# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class RO(Segment):
    """
    RO - Public Record or Obligation
    
    Description:
        To provide details of public records or obligations
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RO/
    """
    _id: Literal["RO"] = id_element(name="RO")

    PublicRecordOrObligationCode: X12ID = element(
        name="RO01",
        description="Public Record or Obligation Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DispositionStatusCode: Optional[X12ID] = element(
        name="RO02",
        description="Disposition Status Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="RO03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="RO04",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="RO05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="RO06",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="RO07",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="RO08",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    TypeOfAccountCode: Optional[X12ID] = element(
        name="RO09",
        description="Type of Account Code",
        min_length=2,
        max_length=2,
    )
