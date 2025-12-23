# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ARS(Segment):
    """
    ARS - Applicant Residence Specifics
    
    Description:
        To provide type of residency
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ARS/
    """
    _id: Literal["ARS"] = id_element(name="ARS")

    TypeOfResidenceCode: X12ID = element(
        name="ARS01",
        description="Type of Residence Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PropertyOwnershipRightsCode: X12ID = element(
        name="ARS02",
        description="Property Ownership Rights Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="ARS03",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="ARS04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ARS05",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
