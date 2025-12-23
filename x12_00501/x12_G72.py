# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G72(Segment):
    """
    G72 - Allowance or Charge
    
    Description:
        To specify allowances, charges, or services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G72/
    """
    _id: Literal["G72"] = id_element(name="G72")

    AllowanceOrChargeCode: X12ID = element(
        name="G7201",
        description="Allowance or Charge Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    AllowanceOrChargeMethodOfHandlingCode: X12ID = element(
        name="G7202",
        description="Allowance or Charge Method of Handling Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AllowanceOrChargeNumber: Optional[X12AN] = element(
        name="G7203",
        description="Allowance or Charge Number",
        min_length=1,
        max_length=16,
    )

    ExceptionNumber: Optional[X12AN] = element(
        name="G7204",
        description="Exception Number",
        min_length=1,
        max_length=16,
    )

    AllowanceOrChargeRate: Optional[X12R] = element(
        name="G7205",
        description="Allowance or Charge Rate",
        min_length=1,
        max_length=15,
    )

    AllowanceOrChargeQuantity: Optional[X12R] = element(
        name="G7206",
        description="Allowance or Charge Quantity",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G7207",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    AllowanceOrChargeTotalAmount: Optional[X12Nn] = element(
        name="G7208",
        description="Allowance or Charge Total Amount",
        min_length=1,
        max_length=15,
    )

    PercentDecimalFormat: Optional[X12R] = element(
        name="G7209",
        description="Percent, Decimal Format",
        min_length=1,
        max_length=6,
    )

    DollarBasisForPercent: Optional[X12R] = element(
        name="G7210",
        description="Dollar Basis For Percent",
        min_length=1,
        max_length=9,
    )

    OptionNumber: Optional[X12AN] = element(
        name="G7211",
        description="Option Number",
        min_length=1,
        max_length=20,
    )
