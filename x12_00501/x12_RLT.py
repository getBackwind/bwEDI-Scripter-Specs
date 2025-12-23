# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class RLT(Segment):
    """
    RLT - Real Estate Loan Type
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RLT/
    """
    _id: Literal["RLT"] = id_element(name="RLT")

    ReferenceIdentificationQualifier: X12ID = element(
        name="RLT01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="RLT02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="RLT03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="RLT04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    RealEstateLoanTypeCode: Optional[X12ID] = element(
        name="RLT05",
        description="Real Estate Loan Type Code",
        min_length=1,
        max_length=1,
    )

    LoanPaymentTypeCode: Optional[X12ID] = element(
        name="RLT06",
        description="Loan Payment Type Code",
        min_length=2,
        max_length=2,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="RLT07",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="RLT08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ReferenceIdentificationQualifier3: Optional[X12ID] = element(
        name="RLT10",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="RLT11",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ProgramTypeCode: Optional[X12ID] = element(
        name="RLT12",
        description="Program Type Code",
        min_length=2,
        max_length=2,
    )
