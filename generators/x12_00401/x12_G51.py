# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class G51(Segment):
    """
    G51 - Free Goods/Product Condition
    
    Description:
        To indicate quantity of free goods and under what conditions free goods are earned
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G51/
    """
    _id: Literal["G51"] = id_element(name="G51")

    QuantityFree: Optional[X12Nn] = element(
        name="G5101",
        description="Quantity Free",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G5102",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    QuantityMustPurchase: X12Nn = element(
        name="G5103",
        description="Quantity Must Purchase",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode2: X12ID = element(
        name="G5104",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="G5105",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    UPCEANConsumerPackageCode: Optional[X12AN] = element(
        name="G5106",
        description="U.P.C./EAN Consumer Package Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G5107",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G5108",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
