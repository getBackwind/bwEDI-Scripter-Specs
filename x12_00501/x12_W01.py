# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class W01(Segment):
    """
    W01 - Line Item Detail - Warehouse
    
    Description:
        To transmit basic and most frequent shipment-related line-item data elements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W01/
    """
    _id: Literal["W01"] = id_element(name="W01")

    Quantity: X12R = element(
        name="W0101",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="W0102",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="W0103",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="W0104",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="W0105",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="W0106",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="W0107",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    FreightClassCode: Optional[X12AN] = element(
        name="W0108",
        description="Freight Class Code",
        min_length=2,
        max_length=5,
    )

    RateClassCode: Optional[X12ID] = element(
        name="W0109",
        description="Rate Class Code",
        min_length=1,
        max_length=3,
    )

    CommodityCodeQualifier: Optional[X12ID] = element(
        name="W0110",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="W0111",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    PalletBlockAndTiers: Optional[X12Nn] = element(
        name="W0112",
        description="Pallet Block and Tiers",
        min_length=6,
        max_length=6,
    )

    WarehouseLotNumber: Optional[X12AN] = element(
        name="W0113",
        description="Warehouse Lot Number",
        min_length=1,
        max_length=12,
    )

    ProductServiceConditionCode: Optional[X12ID] = element(
        name="W0114",
        description="Product/Service Condition Code",
        min_length=2,
        max_length=2,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="W0115",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="W0116",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
