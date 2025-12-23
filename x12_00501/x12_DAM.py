# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class DAM(Segment):
    """
    DAM - Damage Information
    
    Description:
        To identify the part of the vehicle that was damaged
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DAM/
    """
    _id: Literal["DAM"] = id_element(name="DAM")

    DamageStatusCode: Optional[X12ID] = element(
        name="DAM01",
        description="Damage Status Code",
        min_length=2,
        max_length=2,
    )

    DamageAreaCode: Optional[X12ID] = element(
        name="DAM02",
        description="Damage Area Code",
        min_length=2,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="DAM03",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="DAM04",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    DamageStatusCode2: Optional[X12ID] = element(
        name="DAM05",
        description="Damage Status Code",
        min_length=2,
        max_length=2,
    )

    DamageAreaCode2: Optional[X12ID] = element(
        name="DAM06",
        description="Damage Area Code",
        min_length=2,
        max_length=2,
    )

    Amount2: Optional[X12Nn] = element(
        name="DAM07",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    DamageStatusCode3: Optional[X12ID] = element(
        name="DAM08",
        description="Damage Status Code",
        min_length=2,
        max_length=2,
    )

    DamageAreaCode3: Optional[X12ID] = element(
        name="DAM09",
        description="Damage Area Code",
        min_length=2,
        max_length=2,
    )

    Amount3: Optional[X12Nn] = element(
        name="DAM10",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    DamageStatusCode4: Optional[X12ID] = element(
        name="DAM11",
        description="Damage Status Code",
        min_length=2,
        max_length=2,
    )

    DamageAreaCode4: Optional[X12ID] = element(
        name="DAM12",
        description="Damage Area Code",
        min_length=2,
        max_length=2,
    )

    Amount4: Optional[X12Nn] = element(
        name="DAM13",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    DamageStatusCode5: Optional[X12ID] = element(
        name="DAM14",
        description="Damage Status Code",
        min_length=2,
        max_length=2,
    )

    DamageAreaCode5: Optional[X12ID] = element(
        name="DAM15",
        description="Damage Area Code",
        min_length=2,
        max_length=2,
    )

    Amount5: Optional[X12Nn] = element(
        name="DAM16",
        description="Amount",
        min_length=1,
        max_length=15,
    )
