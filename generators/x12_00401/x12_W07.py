# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class W07(Segment):
    """
    W07 - Item Detail For Stock Receipt
    
    Description:
        To indicate quantity and condition of product received
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W07/
    """
    _id: Literal["W07"] = id_element(name="W07")

    QuantityReceived: X12R = element(
        name="W0701",
        description="Quantity Received",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="W0702",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="W0703",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="W0704",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="W0705",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="W0706",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="W0707",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    WarehouseLotNumber: Optional[X12AN] = element(
        name="W0708",
        description="Warehouse Lot Number",
        min_length=1,
        max_length=12,
    )

    WarehouseDetailAdjustmentIdentifier: Optional[X12ID] = element(
        name="W0709",
        description="Warehouse Detail Adjustment Identifier",
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="W0710",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="W0711",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
