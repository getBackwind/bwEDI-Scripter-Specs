# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PKL(Segment):
    """
    PKL - Multi-Pack Configuration
    
    Description:
        To identify the package level, quantity of stock-keeping units (SKUs), and other basic data related to the configuration of the package being defined
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PKL/
    """
    _id: Literal["PKL"] = id_element(name="PKL")

    ProductServiceIDQualifier: X12ID = element(
        name="PKL01",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="PKL02",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="PKL03",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: X12R = element(
        name="PKL04",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Height: Optional[X12R] = element(
        name="PKL05",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="PKL06",
        description="Width",
        min_length=1,
        max_length=8,
    )

    ItemDepth: Optional[X12R] = element(
        name="PKL07",
        description="Item Depth",
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="PKL08",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    GrossWeightPerPack: Optional[X12R] = element(
        name="PKL09",
        description="Gross Weight per Pack",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="PKL10",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    GrossVolumePerPack: Optional[X12R] = element(
        name="PKL11",
        description="Gross Volume per Pack",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="PKL12",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PKL13",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
