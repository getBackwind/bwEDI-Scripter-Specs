# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G83(Segment):
    """
    G83 - Line Item Detail/Direct Store Delivery
    
    Description:
        To specify the basic, and most frequently used line item data for the delivery record transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G83/
    """
    _id: Literal["G83"] = id_element(name="G83")

    DirectStoreDeliverySequenceNumber: X12Nn = element(
        name="G8301",
        description="Direct Store Delivery Sequence Number",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    Quantity: X12R = element(
        name="G8302",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="G8303",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    UPCEANConsumerPackageCode: Optional[X12AN] = element(
        name="G8304",
        description="U.P.C./EAN Consumer Package Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G8305",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G8306",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="G8307",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ItemListCost: Optional[X12R] = element(
        name="G8308",
        description="Item List Cost",
        min_length=1,
        max_length=9,
    )

    Pack: Optional[X12Nn] = element(
        name="G8309",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    CashRegisterItemDescription: Optional[X12AN] = element(
        name="G8310",
        description="Cash Register Item Description",
        min_length=1,
        max_length=20,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="G8311",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="G8312",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    InnerPack: Optional[X12Nn] = element(
        name="G8313",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )
