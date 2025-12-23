# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BAU(Segment):
    """
    BAU - Beginning Segment for the Debit Authorization
    
    Description:
        To identify the beginning of the Debit Authorization Transaction Set; the BAU segment is used to identify the financial institution and account of the payer (i.e., the party authorizing the debit against its account)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BAU/
    """
    _id: Literal["BAU"] = id_element(name="BAU")

    ReferenceIdentification: X12AN = element(
        name="BAU01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    PaymentMethodCode: X12ID = element(
        name="BAU02",
        description="Payment Method Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DFIIDNumberQualifier: X12ID = element(
        name="BAU03",
        description="(DFI) ID Number Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber: X12AN = element(
        name="BAU04",
        description="(DFI) Identification Number",
        mandatory=True,
        min_length=3,
        max_length=12,
    )

    AccountNumber: X12AN = element(
        name="BAU05",
        description="Account Number",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    Name: Optional[X12AN] = element(
        name="BAU06",
        description="Name",
        min_length=1,
        max_length=60,
    )
