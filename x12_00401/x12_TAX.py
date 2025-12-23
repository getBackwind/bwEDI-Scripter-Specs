# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TAX(Segment):
    """
    TAX - Tax Reference
    
    Description:
        To provide data required for proper notification/determination of applicable taxes applying to the transaction or business described in the transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TAX/
    """
    _id: Literal["TAX"] = id_element(name="TAX")

    TaxIdentificationNumber: Optional[X12AN] = element(
        name="TAX01",
        description="Tax Identification Number",
        min_length=1,
        max_length=20,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="TAX02",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="TAX03",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationQualifier2: Optional[X12ID] = element(
        name="TAX04",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="TAX05",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationQualifier3: Optional[X12ID] = element(
        name="TAX06",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier3: Optional[X12AN] = element(
        name="TAX07",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationQualifier4: Optional[X12ID] = element(
        name="TAX08",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier4: Optional[X12AN] = element(
        name="TAX09",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationQualifier5: Optional[X12ID] = element(
        name="TAX10",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier5: Optional[X12AN] = element(
        name="TAX11",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    TaxExemptCode: Optional[X12ID] = element(
        name="TAX12",
        description="Tax Exempt Code",
        min_length=1,
        max_length=1,
    )

    CustomsEntryTypeGroupCode: Optional[X12ID] = element(
        name="TAX13",
        description="Customs Entry Type Group Code",
        min_length=1,
        max_length=1,
    )
