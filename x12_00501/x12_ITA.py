# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class ITA(Segment):
    """
    ITA - Allowance, Charge or Service
    
    Description:
        To specify allowances, charges, or services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ITA/
    """
    _id: Literal["ITA"] = id_element(name="ITA")

    AllowanceOrChargeIndicator: X12ID = element(
        name="ITA01",
        description="Allowance or Charge Indicator",
        mandatory=True,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="ITA02",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SpecialServicesCode: Optional[X12ID] = element(
        name="ITA03",
        description="Special Services Code",
        min_length=2,
        max_length=3,
    )

    AllowanceOrChargeMethodOfHandlingCode: X12ID = element(
        name="ITA04",
        description="Allowance or Charge Method of Handling Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AllowanceOrChargeNumber: Optional[X12AN] = element(
        name="ITA05",
        description="Allowance or Charge Number",
        min_length=1,
        max_length=16,
    )

    AllowanceOrChargeRate: Optional[X12R] = element(
        name="ITA06",
        description="Allowance or Charge Rate",
        min_length=1,
        max_length=15,
    )

    AllowanceOrChargeTotalAmount: Optional[X12Nn] = element(
        name="ITA07",
        description="Allowance or Charge Total Amount",
        min_length=1,
        max_length=15,
    )

    AllowanceChargePercentQualifier: Optional[X12ID] = element(
        name="ITA08",
        description="Allowance/Charge Percent Qualifier",
        min_length=1,
        max_length=1,
    )

    PercentDecimalFormat: Optional[X12R] = element(
        name="ITA09",
        description="Percent, Decimal Format",
        min_length=1,
        max_length=6,
    )

    Quantity: Optional[X12R] = element(
        name="ITA10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="ITA11",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity2: Optional[X12R] = element(
        name="ITA12",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="ITA13",
        description="Description",
        min_length=1,
        max_length=80,
    )

    SpecialChargeOrAllowanceCode: Optional[X12ID] = element(
        name="ITA14",
        description="Special Charge or Allowance Code",
        min_length=3,
        max_length=3,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="ITA15",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    RelationshipCode: Optional[X12ID] = element(
        name="ITA16",
        description="Relationship Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="ITA17",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
