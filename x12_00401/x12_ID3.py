# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class ID3(Segment):
    """
    ID3 - Dimensions Detail
    
    Description:
        To provide information about the physical dimensions of the case
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ID3/
    """
    _id: Literal["ID3"] = id_element(name="ID3")

    UPCCaseCode: Optional[X12AN] = element(
        name="ID301",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="ID302",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="ID303",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Pack: Optional[X12Nn] = element(
        name="ID304",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    InnerPack: Optional[X12Nn] = element(
        name="ID305",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )

    Height: Optional[X12R] = element(
        name="ID306",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="ID307",
        description="Width",
        min_length=1,
        max_length=8,
    )

    ItemDepth: Optional[X12R] = element(
        name="ID308",
        description="Item Depth",
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="ID309",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="ID310",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="ID311",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="ID312",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="ID313",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    TrayCount: Optional[X12Nn] = element(
        name="ID314",
        description="Tray Count",
        min_length=1,
        max_length=3,
    )

    Height2: Optional[X12R] = element(
        name="ID315",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width2: Optional[X12R] = element(
        name="ID316",
        description="Width",
        min_length=1,
        max_length=8,
    )

    ItemDepth2: Optional[X12R] = element(
        name="ID317",
        description="Item Depth",
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="ID318",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    NestingCode: Optional[X12ID] = element(
        name="ID319",
        description="Nesting Code",
        min_length=1,
        max_length=1,
    )

    Nesting: Optional[X12R] = element(
        name="ID320",
        description="Nesting",
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="ID321",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
