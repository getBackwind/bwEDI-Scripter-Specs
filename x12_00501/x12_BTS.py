# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class BTS(Segment):
    """
    BTS - Beginning Segment for Train Sheets
    
    Description:
        To transmit identifying symbols, loads, empties, weights, lengths, horsepower, and related data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BTS/
    """
    _id: Literal["BTS"] = id_element(name="BTS")

    InterchangeTrainIdentification: X12AN = element(
        name="BTS01",
        description="Interchange Train Identification",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    TotalEquipment: Optional[X12Nn] = element(
        name="BTS02",
        description="Total Equipment",
        min_length=1,
        max_length=3,
    )

    EquipmentStatusCode: Optional[X12ID] = element(
        name="BTS03",
        description="Equipment Status Code",
        min_length=1,
        max_length=2,
    )

    TotalEquipment2: Optional[X12Nn] = element(
        name="BTS04",
        description="Total Equipment",
        min_length=1,
        max_length=3,
    )

    EquipmentStatusCode2: Optional[X12ID] = element(
        name="BTS05",
        description="Equipment Status Code",
        min_length=1,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="BTS06",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Length: Optional[X12R] = element(
        name="BTS07",
        description="Length",
        min_length=1,
        max_length=8,
    )

    Horsepower: Optional[X12Nn] = element(
        name="BTS08",
        description="Horsepower",
        min_length=1,
        max_length=16,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="BTS09",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BTS10",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ServiceLevelCode: Optional[X12ID] = element(
        name="BTS11",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="BTS12",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="BTS13",
        description="Date",
        min_length=8,
        max_length=8,
    )

    InterchangeTrainIdentification2: Optional[X12AN] = element(
        name="BTS14",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )

    Number: Optional[X12Nn] = element(
        name="BTS15",
        description="Number",
        min_length=1,
        max_length=9,
    )
