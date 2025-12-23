# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class SAC(Segment):
    """
    SAC - Service, Promotion, Allowance, or Charge Information
    
    Description:
        To request or identify a service, promotion, allowance, or charge; to specify the amount or percentage for the service, promotion, allowance, or charge
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SAC/
    """
    _id: Literal["SAC"] = id_element(name="SAC")

    ChargeIndicator: X12ID = element(
        name="SAC01",
        description="Allowance or Charge Indicator",
        mandatory=True,
    )

    SpecialServiceCode: Optional[X12ID] = element(
        name="SAC02",
        description="Service, Promotion, Allowance, or Charge Code",
    )

    AgencyQualifier: Optional[X12ID] = element(
        name="SAC03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    Agency: Optional[X12AN] = element(
        name="SAC04",
        description="Agency Service, Promotion, Allowance, or Charge Code",
        min_length=1,
        max_length=10,
    )

    Amount: Optional[X12Nn] = element(
        name="SAC05",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    AllowanceChargePercentQualifier: Optional[X12ID] = element(
        name="SAC06",
        description="Allowance/Charge Percent Qualifier",
        min_length=1,
        max_length=1,
    )

    PercentDecimalFormat: Optional[X12R] = element(
        name="SAC07",
        description="Percent, Decimal Format",
        min_length=1,
        max_length=6,
    )

    Rate: Optional[X12R] = element(
        name="SAC08",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="SAC09",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="SAC10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="SAC11",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AllowanceOrChargeMethodOfHandlingCode: Optional[X12ID] = element(
        name="SAC12",
        description="Allowance or Charge Method of Handling Code",
        min_length=2,
        max_length=2,
    )

    ReferenceID: Optional[X12AN] = element(
        name="SAC13",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    OptionNumber: Optional[X12AN] = element(
        name="SAC14",
        description="Option Number",
        min_length=1,
        max_length=20,
    )

    Description: Optional[X12AN] = element(
        name="SAC15",
        description="Description",
        min_length=1,
        max_length=80,
    )

    LanguageCode: Optional[X12ID] = element(
        name="SAC16",
        description="Language Code",
        min_length=2,
        max_length=3,
    )
