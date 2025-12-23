# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CN1(Segment):
    """
    CN1 - Contract Information
    
    Description:
        To specify basic data about the contract or contract line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CN1/
    """
    _id: Literal["CN1"] = id_element(name="CN1")

    ContractTypeCode: X12ID = element(
        name="CN101",
        description="Contract Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Amount: Optional[X12R] = element(
        name="CN102",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12R] = element(
        name="CN103",
        description="Percent",
        min_length=1,
        max_length=6,
    )

    ReferenceID: Optional[X12AN] = element(
        name="CN104",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    TermsDiscountID: Optional[X12R] = element(
        name="CN105",
        description="Terms Discount Percent",
        min_length=1,
        max_length=6,
    )

    VersionID: Optional[X12AN] = element(
        name="CN106",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )
