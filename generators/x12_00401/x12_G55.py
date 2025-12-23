# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G55(Segment):
    """
    G55 - Item Characteristics - Consumer Unit
    
    Description:
        To provide physical characteristics relative to a consumer unit
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G55/
    """
    _id: Literal["G55"] = id_element(name="G55")

    ProductServiceIDQualifier: X12ID = element(
        name="G5501",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="G5502",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="G5503",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="G5504",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Height: Optional[X12R] = element(
        name="G5505",
        description="Height",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G5506",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Width: Optional[X12R] = element(
        name="G5507",
        description="Width",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="G5508",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Length: Optional[X12R] = element(
        name="G5509",
        description="Length",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="G5510",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="G5511",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="G5512",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Pack: Optional[X12Nn] = element(
        name="G5513",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    Size: Optional[X12R] = element(
        name="G5514",
        description="Size",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="G5515",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    CashRegisterItemDescription: Optional[X12AN] = element(
        name="G5516",
        description="Cash Register Item Description",
        min_length=1,
        max_length=20,
    )

    CashRegisterItemDescription2: Optional[X12AN] = element(
        name="G5517",
        description="Cash Register Item Description",
        min_length=1,
        max_length=20,
    )

    CouponFamilyCode: Optional[X12AN] = element(
        name="G5518",
        description="Coupon Family Code",
        min_length=3,
        max_length=3,
    )

    DatedProductNumberOfDays: Optional[X12Nn] = element(
        name="G5519",
        description="Dated Product Number of Days",
        min_length=1,
        max_length=4,
    )

    DepositValue: Optional[X12R] = element(
        name="G5520",
        description="Deposit Value",
        min_length=1,
        max_length=8,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="G5521",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Color: Optional[X12AN] = element(
        name="G5522",
        description="Color",
        min_length=1,
        max_length=10,
    )

    UnitWeight: Optional[X12R] = element(
        name="G5523",
        description="Unit Weight",
        min_length=1,
        max_length=8,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="G5524",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="G5525",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    UnitWeight2: Optional[X12R] = element(
        name="G5526",
        description="Unit Weight",
        min_length=1,
        max_length=8,
    )

    WeightQualifier2: Optional[X12ID] = element(
        name="G5527",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode2: Optional[X12ID] = element(
        name="G5528",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="G5529",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="G5530",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="G5531",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    InnerPack: Optional[X12Nn] = element(
        name="G5532",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )

    PackagingCode: Optional[X12AN] = element(
        name="G5533",
        description="Packaging Code",
        min_length=3,
        max_length=5,
    )
