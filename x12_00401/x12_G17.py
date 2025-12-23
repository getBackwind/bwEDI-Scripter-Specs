# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class G17(Segment):
    """
    G17 - Item Detail - Invoice
    
    Description:
        To specify the basic and most frequently used line item data for the invoice and related transactions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G17/
    """
    _id: Literal["G17"] = id_element(name="G17")

    QuantityInvoiced: X12R = element(
        name="G1701",
        description="Quantity Invoiced",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="G1702",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ItemListCost: Optional[X12R] = element(
        name="G1703",
        description="Item List Cost",
        min_length=1,
        max_length=9,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="G1704",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G1705",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G1706",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="G1707",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="G1708",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    PriceBracketIdentifier: Optional[X12AN] = element(
        name="G1709",
        description="Price Bracket Identifier",
        min_length=1,
        max_length=3,
    )

    NumberOfUnitsShipped: Optional[X12R] = element(
        name="G1710",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="G1711",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PriceListNumber: Optional[X12AN] = element(
        name="G1712",
        description="Price List Number",
        min_length=1,
        max_length=16,
    )

    PriceListIssueNumber: Optional[X12AN] = element(
        name="G1713",
        description="Price List Issue Number",
        min_length=1,
        max_length=16,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="G1714",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
