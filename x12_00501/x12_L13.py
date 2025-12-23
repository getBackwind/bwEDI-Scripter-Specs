# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class L13(Segment):
    """
    L13 - Commodity Details
    
    Description:
        To specify the commodity details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/L13/
    """
    _id: Literal["L13"] = id_element(name="L13")

    CommodityCodeQualifier: X12ID = element(
        name="L1301",
        description="Commodity Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CommodityCode: X12AN = element(
        name="L1302",
        description="Commodity Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="L1303",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: X12R = element(
        name="L1304",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    AmountQualifierCode: X12ID = element(
        name="L1305",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="L1306",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    AssignedNumber: X12Nn = element(
        name="L1307",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="L1308",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity2: Optional[X12R] = element(
        name="L1309",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="L1310",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="L1311",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="L1312",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    ExportExceptionCode: Optional[X12ID] = element(
        name="L1313",
        description="Export Exception Code",
    )

    ActionCode: Optional[X12ID] = element(
        name="L1314",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    HarborMaintenanceFeeHMFExemptionCode: Optional[X12AN] = element(
        name="L1315",
        description="Harbor Maintenance Fee (HMF) Exemption Code",
        min_length=1,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="L1316",
        description="Amount",
        min_length=1,
        max_length=15,
    )
