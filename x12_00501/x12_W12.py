# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class W12(Segment):
    """
    W12 - Warehouse Item Detail
    
    Description:
        To designate those line items that were shipped
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W12/
    """
    _id: Literal["W12"] = id_element(name="W12")

    ShipmentOrderStatusCode: X12ID = element(
        name="W1201",
        description="Shipment/Order Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="W1202",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    NumberOfUnitsShipped: Optional[X12R] = element(
        name="W1203",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    QuantityDifference: Optional[X12R] = element(
        name="W1204",
        description="Quantity Difference",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="W1205",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="W1206",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="W1207",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="W1208",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    WarehouseLotNumber: Optional[X12AN] = element(
        name="W1209",
        description="Warehouse Lot Number",
        min_length=1,
        max_length=12,
    )

    Weight: Optional[X12R] = element(
        name="W1210",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="W1211",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="W1212",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight2: Optional[X12R] = element(
        name="W1213",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier2: Optional[X12ID] = element(
        name="W1214",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode2: Optional[X12ID] = element(
        name="W1215",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    UPCCaseCode2: Optional[X12AN] = element(
        name="W1216",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="W1217",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="W1218",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    LineItemChangeReasonCode: Optional[X12ID] = element(
        name="W1219",
        description="Line Item Change Reason Code",
        min_length=2,
        max_length=2,
    )

    WarehouseDetailAdjustmentIdentifier: Optional[X12ID] = element(
        name="W1220",
        description="Warehouse Detail Adjustment Identifier",
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="W1221",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="W1222",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
