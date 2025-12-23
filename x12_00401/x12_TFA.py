# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class TFA(Segment):
    """
    TFA - Tariff Adjustments
    
    Description:
        To transmit tariff adjustment values
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TFA/
    """
    _id: Literal["TFA"] = id_element(name="TFA")

    RateValueQualifier: X12ID = element(
        name="TFA01",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TariffAdjustmentValueAmount: Optional[X12R] = element(
        name="TFA02",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount2: Optional[X12R] = element(
        name="TFA03",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount3: Optional[X12R] = element(
        name="TFA04",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount4: Optional[X12R] = element(
        name="TFA05",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount5: Optional[X12R] = element(
        name="TFA06",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount6: Optional[X12R] = element(
        name="TFA07",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount7: Optional[X12R] = element(
        name="TFA08",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount8: Optional[X12R] = element(
        name="TFA09",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount9: Optional[X12R] = element(
        name="TFA10",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount10: Optional[X12R] = element(
        name="TFA11",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount11: Optional[X12R] = element(
        name="TFA12",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount12: Optional[X12R] = element(
        name="TFA13",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount13: Optional[X12R] = element(
        name="TFA14",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount14: Optional[X12R] = element(
        name="TFA15",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount15: Optional[X12R] = element(
        name="TFA16",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )

    TariffAdjustmentValueAmount16: Optional[X12R] = element(
        name="TFA17",
        description="Tariff Adjustment Value/Amount",
        min_length=1,
        max_length=9,
    )
