# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PS(Segment):
    """
    PS - Protective Service Instructions
    
    Description:
        To specify mechanical protective service and ventilation instructions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PS/
    """
    _id: Literal["PS"] = id_element(name="PS")

    ProtectiveServiceRuleCode: X12ID = element(
        name="PS01",
        description="Protective Service Rule Code",
        mandatory=True,
        min_length=3,
        max_length=9,
    )

    ProtectiveServiceCode: X12ID = element(
        name="PS02",
        description="Protective Service Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="PS03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Temperature: Optional[X12R] = element(
        name="PS04",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="PS05",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    FreightStationAccountingCode: Optional[X12ID] = element(
        name="PS06",
        description="Freight Station Accounting Code",
        min_length=1,
        max_length=5,
    )

    CityName: Optional[X12AN] = element(
        name="PS07",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="PS08",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="PS09",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    PreCooledRule710Code: Optional[X12ID] = element(
        name="PS10",
        description="Pre-Cooled (Rule 710) Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PS11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="PS12",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="PS13",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Temperature2: Optional[X12R] = element(
        name="PS14",
        description="Temperature",
        min_length=1,
        max_length=4,
    )
