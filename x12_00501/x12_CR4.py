# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CR4(Segment):
    """
    CR4 - Enteral or Parenteral Therapy Certification
    
    Description:
        To supply information regarding certification of medical necessity for enteral or parenteral nutrition therapy
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CR4/
    """
    _id: Literal["CR4"] = id_element(name="CR4")

    YesNoConditionOrResponseCode: X12ID = element(
        name="CR401",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CertificationTypeCode: Optional[X12ID] = element(
        name="CR402",
        description="Certification Type Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="CR403",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="CR404",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="CR405",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity2: Optional[X12R] = element(
        name="CR406",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    NonVisitCode: Optional[X12ID] = element(
        name="CR407",
        description="Non-Visit Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="CR408",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity3: Optional[X12R] = element(
        name="CR409",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode4: Optional[X12ID] = element(
        name="CR410",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Height: Optional[X12R] = element(
        name="CR411",
        description="Height",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode5: Optional[X12ID] = element(
        name="CR412",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="CR413",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Quantity4: Optional[X12R] = element(
        name="CR414",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="CR415",
        description="Description",
        min_length=1,
        max_length=80,
    )

    NutrientAdministrationMethodCode: Optional[X12ID] = element(
        name="CR416",
        description="Nutrient Administration Method Code",
        min_length=1,
        max_length=1,
    )

    NutrientAdministrationTechniqueCode: Optional[X12ID] = element(
        name="CR417",
        description="Nutrient Administration Technique Code",
        min_length=1,
        max_length=1,
    )

    Quantity5: Optional[X12R] = element(
        name="CR418",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity6: Optional[X12R] = element(
        name="CR419",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Description2: Optional[X12AN] = element(
        name="CR420",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Quantity7: Optional[X12R] = element(
        name="CR421",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="CR422",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    Quantity8: Optional[X12R] = element(
        name="CR423",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity9: Optional[X12R] = element(
        name="CR424",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PercentageAsDecimal2: Optional[X12R] = element(
        name="CR425",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    Quantity10: Optional[X12R] = element(
        name="CR426",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PercentageAsDecimal3: Optional[X12R] = element(
        name="CR427",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    Quantity11: Optional[X12R] = element(
        name="CR428",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Description3: Optional[X12AN] = element(
        name="CR429",
        description="Description",
        min_length=1,
        max_length=80,
    )
