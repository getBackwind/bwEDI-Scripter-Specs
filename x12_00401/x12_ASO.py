# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ASO(Segment):
    """
    ASO - Asset Ownership
    
    Description:
        To describe ownership of and identify type of assets utilized or owned
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ASO/
    """
    _id: Literal["ASO"] = id_element(name="ASO")

    PropertyOwnershipRightsCode: X12ID = element(
        name="ASO01",
        description="Property Ownership Rights Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    TypeOfPersonalOrBusinessAssetCode: X12ID = element(
        name="ASO02",
        description="Type of Personal or Business Asset Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TypeOfPersonalOrBusinessAssetCode2: Optional[X12ID] = element(
        name="ASO03",
        description="Type of Personal or Business Asset Code",
        min_length=2,
        max_length=2,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="ASO04",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )

    GeneralPropertyOwnershipCode: Optional[X12ID] = element(
        name="ASO05",
        description="General Property Ownership Code",
        min_length=1,
        max_length=1,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="ASO07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12R] = element(
        name="ASO08",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    Quantity: Optional[X12R] = element(
        name="ASO09",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="ASO10",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ASO11",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
