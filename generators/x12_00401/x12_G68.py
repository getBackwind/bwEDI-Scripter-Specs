# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G68(Segment):
    """
    G68 - Line Item Detail - Product
    
    Description:
        To specify basic and most frequently used purchase order line item data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G68/
    """
    _id: Literal["G68"] = id_element(name="G68")

    QuantityOrdered: X12R = element(
        name="G6801",
        description="Quantity Ordered",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="G6802",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ItemListCost: Optional[X12R] = element(
        name="G6803",
        description="Item List Cost",
        min_length=1,
        max_length=9,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="G6804",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G6805",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G6806",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="G6807",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="G6808",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    PriceBracketIdentifier: Optional[X12AN] = element(
        name="G6809",
        description="Price Bracket Identifier",
        min_length=1,
        max_length=3,
    )

    QuantityCost: Optional[X12Nn] = element(
        name="G6810",
        description="Quantity Cost",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="G6811",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PriceListNumber: Optional[X12AN] = element(
        name="G6812",
        description="Price List Number",
        min_length=1,
        max_length=16,
    )

    PriceListIssueNumber: Optional[X12AN] = element(
        name="G6813",
        description="Price List Issue Number",
        min_length=1,
        max_length=16,
    )

    PrePriceQuantityDesignator: Optional[X12Nn] = element(
        name="G6814",
        description="Pre-Price Quantity Designator",
        min_length=1,
        max_length=9,
    )

    RetailPrePrice: Optional[X12R] = element(
        name="G6815",
        description="Retail Pre-Price",
        min_length=1,
        max_length=9,
    )
