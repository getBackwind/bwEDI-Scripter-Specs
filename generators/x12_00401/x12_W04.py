# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class W04(Segment):
    """
    W04 - Item Detail Total
    
    Description:
        To designate those line items that were shipped
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W04/
    """
    _id: Literal["W04"] = id_element(name="W04")

    NumberOfUnitsShipped: X12R = element(
        name="W0401",
        description="Number of Units Shipped",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="W0402",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="W0403",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="W0404",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="W0405",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="W0406",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="W0407",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    FreightClassCode: Optional[X12AN] = element(
        name="W0408",
        description="Freight Class Code",
        min_length=2,
        max_length=5,
    )

    RateClassCode: Optional[X12ID] = element(
        name="W0409",
        description="Rate Class Code",
        min_length=1,
        max_length=3,
    )

    CommodityCodeQualifier: Optional[X12ID] = element(
        name="W0410",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="W0411",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    PalletBlockAndTiers: Optional[X12Nn] = element(
        name="W0412",
        description="Pallet Block and Tiers",
        min_length=6,
        max_length=6,
    )

    InboundConditionHoldCode: Optional[X12ID] = element(
        name="W0413",
        description="Inbound Condition Hold Code",
        min_length=2,
        max_length=2,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="W0414",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="W0415",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
