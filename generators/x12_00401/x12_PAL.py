# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class PAL(Segment):
    """
    PAL - Pallet Information
    
    Description:
        To identify the type and physical attributes of the pallet, and, gross weight, gross volume, and height of the load and the pallet
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PAL/
    """
    _id: Literal["PAL"] = id_element(name="PAL")

    PalletTypeCode: Optional[X12ID] = element(
        name="PAL01",
        description="Pallet Type Code",
        min_length=1,
        max_length=1,
    )

    PalletTiers: Optional[X12Nn] = element(
        name="PAL02",
        description="Pallet Tiers",
        min_length=1,
        max_length=3,
    )

    PalletBlocks: Optional[X12Nn] = element(
        name="PAL03",
        description="Pallet Blocks",
        min_length=1,
        max_length=3,
    )

    Pack: Optional[X12Nn] = element(
        name="PAL04",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    UnitWeight: Optional[X12R] = element(
        name="PAL05",
        description="Unit Weight",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="PAL06",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Length: Optional[X12R] = element(
        name="PAL07",
        description="Length",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="PAL08",
        description="Width",
        min_length=1,
        max_length=8,
    )

    Height: Optional[X12R] = element(
        name="PAL09",
        description="Height",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="PAL10",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    GrossWeightPerPack: Optional[X12R] = element(
        name="PAL11",
        description="Gross Weight per Pack",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="PAL12",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    GrossVolumePerPack: Optional[X12R] = element(
        name="PAL13",
        description="Gross Volume per Pack",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="PAL14",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PalletExchangeCode: Optional[X12ID] = element(
        name="PAL15",
        description="Pallet Exchange Code",
        min_length=1,
        max_length=1,
    )

    InnerPack: Optional[X12Nn] = element(
        name="PAL16",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )
