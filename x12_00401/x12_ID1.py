# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class ID1(Segment):
    """
    ID1 - Item Detail Dimensions
    
    Description:
        To transmit information about the physical characteristics of items
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ID1/
    """
    _id: Literal["ID1"] = id_element(name="ID1")

    UPCEANConsumerPackageCode: Optional[X12AN] = element(
        name="ID101",
        description="U.P.C./EAN Consumer Package Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="ID102",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="ID103",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    FreeFormDescription: X12AN = element(
        name="ID104",
        description="Free-form Description",
        mandatory=True,
        min_length=1,
        max_length=45,
    )

    Size: X12R = element(
        name="ID105",
        description="Size",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="ID106",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Height: X12R = element(
        name="ID107",
        description="Height",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    Width: X12R = element(
        name="ID108",
        description="Width",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    ItemDepth: X12R = element(
        name="ID109",
        description="Item Depth",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode2: X12ID = element(
        name="ID110",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="ID111",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="ID112",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    CategoryReferenceCode: Optional[X12ID] = element(
        name="ID113",
        description="Category Reference Code",
        min_length=1,
        max_length=1,
    )

    Category: Optional[X12AN] = element(
        name="ID114",
        description="Category",
        min_length=1,
        max_length=6,
    )

    Subcategory: Optional[X12AN] = element(
        name="ID115",
        description="Subcategory",
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="ID116",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Pack: Optional[X12Nn] = element(
        name="ID117",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    InnerPack: Optional[X12Nn] = element(
        name="ID118",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )

    DateQualifier: Optional[X12ID] = element(
        name="ID119",
        description="Date Qualifier",
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="ID120",
        description="Date",
        min_length=8,
        max_length=8,
    )

    NestingCode: Optional[X12ID] = element(
        name="ID121",
        description="Nesting Code",
        min_length=1,
        max_length=1,
    )

    Nesting: Optional[X12R] = element(
        name="ID122",
        description="Nesting",
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="ID123",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    PegCode: Optional[X12ID] = element(
        name="ID124",
        description="Peg Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode6: Optional[X12ID] = element(
        name="ID125",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ID126",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    XPeg: Optional[X12R] = element(
        name="ID127",
        description="X-Peg",
        min_length=1,
        max_length=6,
    )

    YPeg: Optional[X12R] = element(
        name="ID128",
        description="Y-Peg",
        min_length=1,
        max_length=6,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="ID129",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    XPeg2: Optional[X12R] = element(
        name="ID130",
        description="X-Peg",
        min_length=1,
        max_length=6,
    )

    YPeg2: Optional[X12R] = element(
        name="ID131",
        description="Y-Peg",
        min_length=1,
        max_length=6,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="ID132",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    XPeg3: Optional[X12R] = element(
        name="ID133",
        description="X-Peg",
        min_length=1,
        max_length=6,
    )

    YPeg3: Optional[X12R] = element(
        name="ID134",
        description="Y-Peg",
        min_length=1,
        max_length=6,
    )
