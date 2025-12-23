# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class W19(Segment):
    """
    W19 - Warehouse Adjustment Item Detail
    
    Description:
        To designate those items that were adjusted
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W19/
    """
    _id: Literal["W19"] = id_element(name="W19")

    QuantityOrStatusAdjustmentReasonCode: X12ID = element(
        name="W1901",
        description="Quantity or Status Adjustment Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CreditDebitQuantity: X12R = element(
        name="W1902",
        description="Credit/Debit Quantity",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="W1903",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="W1904",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="W1905",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="W1906",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="W1907",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="W1908",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    WarehouseLotNumber: Optional[X12AN] = element(
        name="W1909",
        description="Warehouse Lot Number",
        min_length=1,
        max_length=12,
    )

    Weight: Optional[X12R] = element(
        name="W1910",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="W1911",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="W1912",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight2: Optional[X12R] = element(
        name="W1913",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier2: Optional[X12ID] = element(
        name="W1914",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode2: Optional[X12ID] = element(
        name="W1915",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    InventoryTransactionTypeCode: Optional[X12ID] = element(
        name="W1916",
        description="Inventory Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="W1917",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="W1918",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
