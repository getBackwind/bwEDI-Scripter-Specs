# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class BTS(Segment):
    """
    BTS - Beginning Segment for Train Sheets
    
    Description:
        To transmit identifying symbols, loads, empties, weights, lengths, horsepower, and related data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BTS/
    """
    _id: Literal["BTS"] = id_element(name="BTS")

    InterchangeTrainIdentification: X12AN = element(
        name="BTS01",
        description="Interchange Train Identification",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    TotalEquipment: X12Nn = element(
        name="BTS02",
        description="Total Equipment",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    EquipmentStatusCode: X12ID = element(
        name="BTS03",
        description="Equipment Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    TotalEquipment2: X12Nn = element(
        name="BTS04",
        description="Total Equipment",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    EquipmentStatusCode2: X12ID = element(
        name="BTS05",
        description="Equipment Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Weight: X12R = element(
        name="BTS06",
        description="Weight",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    Length: X12R = element(
        name="BTS07",
        description="Length",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    Horsepower: X12Nn = element(
        name="BTS08",
        description="Horsepower",
        mandatory=True,
        min_length=1,
        max_length=16,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="BTS09",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    TransactionSetPurposeCode: X12ID = element(
        name="BTS10",
        description="Transaction Set Purpose Code",
        mandatory=True,
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
