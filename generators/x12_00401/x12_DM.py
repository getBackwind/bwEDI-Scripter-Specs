# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R, X12TM


class DM(Segment):
    """
    DM - Demurrage/Detention/ Storage Rate
    
    Description:
        To specify the demurrage, detention, or storage rate in a docket
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DM/
    """
    _id: Literal["DM"] = id_element(name="DM")

    GeographyQualifierCode: X12ID = element(
        name="DM01",
        description="Geography Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RateValueQualifier: X12ID = element(
        name="DM02",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TimeQualifier: Optional[X12ID] = element(
        name="DM03",
        description="Time Qualifier",
        min_length=1,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="DM04",
        description="Time",
        min_length=4,
        max_length=8,
    )

    NumberOfPeriods: X12Nn = element(
        name="DM05",
        description="Number of Periods",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    TimePeriodQualifier: X12ID = element(
        name="DM06",
        description="Time Period Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    NumberOfPeriods2: X12Nn = element(
        name="DM07",
        description="Number of Periods",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    Rate: X12R = element(
        name="DM08",
        description="Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    IntermodalServiceCode: Optional[X12ID] = element(
        name="DM09",
        description="Intermodal Service Code",
        min_length=1,
        max_length=2,
    )

    TariffApplicationCode: Optional[X12ID] = element(
        name="DM10",
        description="Tariff Application Code",
        min_length=1,
        max_length=1,
    )

    BillingCode: Optional[X12ID] = element(
        name="DM11",
        description="Billing Code",
        min_length=1,
        max_length=1,
    )

    TimePeriodQualifier2: Optional[X12ID] = element(
        name="DM12",
        description="Time Period Qualifier",
        min_length=1,
        max_length=2,
    )

    NumberOfPeriods3: Optional[X12Nn] = element(
        name="DM13",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    NumberOfPeriods4: Optional[X12Nn] = element(
        name="DM14",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    Rate2: Optional[X12R] = element(
        name="DM15",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    NumberOfPeriods5: Optional[X12Nn] = element(
        name="DM16",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    Rate3: Optional[X12R] = element(
        name="DM17",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    NumberOfPeriods6: Optional[X12Nn] = element(
        name="DM18",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    Rate4: Optional[X12R] = element(
        name="DM19",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    NumberOfPeriods7: Optional[X12Nn] = element(
        name="DM20",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    Rate5: Optional[X12R] = element(
        name="DM21",
        description="Rate",
        min_length=1,
        max_length=9,
    )
