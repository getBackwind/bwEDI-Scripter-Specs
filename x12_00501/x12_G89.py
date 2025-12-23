# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G89(Segment):
    """
    G89 - Line Item Detail - Adjustment
    
    Description:
        To transmit line-item detail adjustments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G89/
    """
    _id: Literal["G89"] = id_element(name="G89")

    DirectStoreDeliverySequenceNumber: X12Nn = element(
        name="G8901",
        description="Direct Store Delivery Sequence Number",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    Quantity: Optional[X12R] = element(
        name="G8902",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G8903",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UPCEANConsumerPackageCode: Optional[X12AN] = element(
        name="G8904",
        description="U.P.C./EAN Consumer Package Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G8905",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G8906",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="G8907",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ItemListCost: Optional[X12R] = element(
        name="G8908",
        description="Item List Cost",
        min_length=1,
        max_length=9,
    )

    Pack: Optional[X12Nn] = element(
        name="G8909",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    InnerPack: Optional[X12Nn] = element(
        name="G8910",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )
