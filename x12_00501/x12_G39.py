# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G39(Segment):
    """
    G39 - Item Characteristics - Vendor's Selling Unit
    
    Description:
        To identify a vendor's selling unit or to provide physical characteristics relative to a vendor's selling unit
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G39/
    """
    _id: Literal["G39"] = id_element(name="G39")

    UPCCaseCode: Optional[X12AN] = element(
        name="G3901",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G3902",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G3903",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    SpecialHandlingCode: Optional[X12ID] = element(
        name="G3904",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    UnitWeight: Optional[X12R] = element(
        name="G3905",
        description="Unit Weight",
        min_length=1,
        max_length=8,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="G3906",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="G3907",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Height: Optional[X12R] = element(
        name="G3908",
        description="Height",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G3909",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Width: Optional[X12R] = element(
        name="G3910",
        description="Width",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="G3911",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Length: Optional[X12R] = element(
        name="G3912",
        description="Length",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="G3913",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="G3914",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="G3915",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PalletBlockAndTiers: Optional[X12Nn] = element(
        name="G3916",
        description="Pallet Block and Tiers",
        min_length=6,
        max_length=6,
    )

    Pack: Optional[X12Nn] = element(
        name="G3917",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    Size: Optional[X12R] = element(
        name="G3918",
        description="Size",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="G3919",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Color: Optional[X12AN] = element(
        name="G3920",
        description="Color",
        min_length=1,
        max_length=10,
    )

    OrderSizingFactor: Optional[X12R] = element(
        name="G3921",
        description="Order Sizing Factor",
        min_length=1,
        max_length=10,
    )

    AlternateTiersPerPallet: Optional[X12ID] = element(
        name="G3922",
        description="Alternate Tiers per Pallet",
        min_length=1,
        max_length=3,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="G3923",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="G3924",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    WeightQualifier2: Optional[X12ID] = element(
        name="G3925",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    UnitWeight2: Optional[X12R] = element(
        name="G3926",
        description="Unit Weight",
        min_length=1,
        max_length=8,
    )

    InnerPack: Optional[X12Nn] = element(
        name="G3927",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )

    PackagingCode: Optional[X12AN] = element(
        name="G3928",
        description="Packaging Code",
        min_length=3,
        max_length=5,
    )

    CashRegisterItemDescription: Optional[X12AN] = element(
        name="G3929",
        description="Cash Register Item Description",
        min_length=1,
        max_length=20,
    )
