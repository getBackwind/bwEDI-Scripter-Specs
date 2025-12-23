# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G46(Segment):
    """
    G46 - Promotion Allowance/Charge
    
    Description:
        To specify unit amount and method of payment for a charge/allowance for a line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G46/
    """
    _id: Literal["G46"] = id_element(name="G46")

    AllowanceOrChargeCode: X12ID = element(
        name="G4601",
        description="Allowance or Charge Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    AllowanceOrChargeMethodOfHandlingCode: X12ID = element(
        name="G4602",
        description="Allowance or Charge Method of Handling Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AllowanceOrChargeRate: Optional[X12R] = element(
        name="G4603",
        description="Allowance or Charge Rate",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G4604",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="G4605",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    AllowanceChargePercentQualifier: Optional[X12ID] = element(
        name="G4606",
        description="Allowance/Charge Percent Qualifier",
        min_length=1,
        max_length=1,
    )

    PercentDecimalFormat: Optional[X12R] = element(
        name="G4607",
        description="Percent, Decimal Format",
        min_length=1,
        max_length=6,
    )

    ExceptionNumber: Optional[X12AN] = element(
        name="G4608",
        description="Exception Number",
        min_length=1,
        max_length=16,
    )

    OptionNumber: Optional[X12AN] = element(
        name="G4609",
        description="Option Number",
        min_length=1,
        max_length=20,
    )

    Description: Optional[X12AN] = element(
        name="G4610",
        description="Description",
        min_length=1,
        max_length=80,
    )

    PriceIdentifierCode: Optional[X12ID] = element(
        name="G4611",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    Number: Optional[X12Nn] = element(
        name="G4612",
        description="Number",
        min_length=1,
        max_length=9,
    )
