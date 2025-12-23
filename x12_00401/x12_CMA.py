# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class CMA(Segment):
    """
    CMA - Cooperative Market Agreement
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CMA/
    """
    _id: Literal["CMA"] = id_element(name="CMA")

    TransactionTypeCode: X12ID = element(
        name="CMA01",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="CMA02",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="CMA03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="CMA04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Week: X12Nn = element(
        name="CMA05",
        description="Week",
        mandatory=True,
        min_length=4,
        max_length=4,
    )

    MarketAreaCodeQualifier: Optional[X12ID] = element(
        name="CMA06",
        description="Market Area Code Qualifier",
        min_length=3,
        max_length=3,
    )

    MarketAreaCodeIdentifier: Optional[X12AN] = element(
        name="CMA07",
        description="Market Area Code Identifier",
        min_length=1,
        max_length=12,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="CMA08",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    MarketProfile: Optional[X12AN] = element(
        name="CMA09",
        description="Market Profile",
        min_length=1,
        max_length=8,
    )

    ContractNumber: Optional[X12AN] = element(
        name="CMA10",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="CMA11",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )
