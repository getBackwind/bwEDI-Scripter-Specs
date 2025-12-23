# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class LH1(Segment):
    """
    LH1 - Hazardous Identification Information
    
    Description:
        To specify the hazardous commodity identification reference number and quantity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LH1/
    """
    _id: Literal["LH1"] = id_element(name="LH1")

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="LH101",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    LadingQuantity: X12Nn = element(
        name="LH102",
        description="Lading Quantity",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    UNNAIdentificationCode: Optional[X12ID] = element(
        name="LH103",
        description="UN/NA Identification Code",
        min_length=6,
        max_length=6,
    )

    HazardousMaterialsPage: Optional[X12AN] = element(
        name="LH104",
        description="Hazardous Materials Page",
        min_length=1,
        max_length=6,
    )

    CommodityCode: Optional[X12AN] = element(
        name="LH105",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="LH106",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="LH107",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    CompartmentIDCode: Optional[X12ID] = element(
        name="LH108",
        description="Compartment ID Code",
        min_length=1,
        max_length=1,
    )

    ResidueIndicatorCode: Optional[X12ID] = element(
        name="LH109",
        description="Residue Indicator Code",
        min_length=1,
        max_length=1,
    )

    PackingGroupCode: Optional[X12ID] = element(
        name="LH110",
        description="Packing Group Code",
        min_length=1,
        max_length=3,
    )

    InterimHazardousMaterialRegulatoryNumber: Optional[X12AN] = element(
        name="LH111",
        description="Interim Hazardous Material Regulatory Number",
        min_length=1,
        max_length=5,
    )
