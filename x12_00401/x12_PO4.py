# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class PO4(Segment):
    """
    PO4 - Item Physical Details
    
    Description:
        To specify the physical qualities, packaging, weights, and dimensions relating to the item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PO4/
    """
    _id: Literal["PO4"] = id_element(name="PO4")

    ContainerCount: Optional[X12Nn] = element(
        name="PO401",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    Size: Optional[X12R] = element(
        name="PO402",
        description="Size",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="PO403",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PackagingCode: Optional[X12AN] = element(
        name="PO404",
        description="Packaging Code",
        min_length=3,
        max_length=5,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="PO405",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    GrossWeightPerPack: Optional[X12R] = element(
        name="PO406",
        description="Gross Weight per Pack",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="PO407",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    GrossVolumePerPack: Optional[X12R] = element(
        name="PO408",
        description="Gross Volume per Pack",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="PO409",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Length: Optional[X12R] = element(
        name="PO410",
        description="Length",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="PO411",
        description="Width",
        min_length=1,
        max_length=8,
    )

    Height: Optional[X12R] = element(
        name="PO412",
        description="Height",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="PO413",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UnitsPerContainer: Optional[X12Nn] = element(
        name="PO414",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )

    SurfaceLayerPositionCode: Optional[X12ID] = element(
        name="PO415",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="PO416",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    AssignedIdentification2: Optional[X12AN] = element(
        name="PO417",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Number: Optional[X12Nn] = element(
        name="PO418",
        description="Number",
        min_length=1,
        max_length=9,
    )
