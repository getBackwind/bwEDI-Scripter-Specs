# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G70(Segment):
    """
    G70 - Line Item Detail - Miscellaneous
    
    Description:
        To provide for miscellaneous information relative to a line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G70/
    """
    _id: Literal["G70"] = id_element(name="G70")

    Pack: Optional[X12Nn] = element(
        name="G7001",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    Size: Optional[X12R] = element(
        name="G7002",
        description="Size",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G7003",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PurchaseOrderInstructionCode: Optional[X12ID] = element(
        name="G7004",
        description="Purchase Order Instruction Code",
        min_length=2,
        max_length=2,
    )

    PriceReasonCode: Optional[X12ID] = element(
        name="G7005",
        description="Price Reason Code",
        min_length=1,
        max_length=1,
    )

    TermsExceptionCode: Optional[X12ID] = element(
        name="G7006",
        description="Terms Exception Code",
        min_length=2,
        max_length=2,
    )

    TaxExemptCode: Optional[X12ID] = element(
        name="G7007",
        description="Tax Exempt Code",
        min_length=1,
        max_length=1,
    )

    Color: Optional[X12AN] = element(
        name="G7008",
        description="Color",
        min_length=1,
        max_length=10,
    )

    PalletBlockAndTiers: Optional[X12Nn] = element(
        name="G7009",
        description="Pallet Block and Tiers",
        min_length=6,
        max_length=6,
    )

    InnerPack: Optional[X12Nn] = element(
        name="G7010",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )
