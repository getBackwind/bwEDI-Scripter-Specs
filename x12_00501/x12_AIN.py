# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class AIN(Segment):
    """
    AIN - Income
    
    Description:
        To provide type and amount of income obtained
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AIN/
    """
    _id: Literal["AIN"] = id_element(name="AIN")

    TypeOfIncomeCode: X12ID = element(
        name="AIN01",
        description="Type of Income Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    FrequencyCode: X12ID = element(
        name="AIN02",
        description="Frequency Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    MonetaryAmount: X12R = element(
        name="AIN03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="AIN04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="AIN05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="AIN06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="AIN07",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    TaxTreatmentCode: Optional[X12ID] = element(
        name="AIN08",
        description="Tax Treatment Code",
        min_length=1,
        max_length=1,
    )

    EarningsRateOfPay: Optional[X12R] = element(
        name="AIN09",
        description="Earnings Rate of Pay",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="AIN10",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity2: Optional[X12R] = element(
        name="AIN11",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    IndustryCode: Optional[X12AN] = element(
        name="AIN12",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="AIN13",
        description="Description",
        min_length=1,
        max_length=80,
    )
