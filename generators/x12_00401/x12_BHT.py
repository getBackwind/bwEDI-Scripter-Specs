# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BHT(Segment):
    """
    BHT - Beginning of Hierarchical Transaction
    
    Description:
        To define the business hierarchical structure of the transaction set and identify the business application purpose and reference data, i.e., number, date, and time
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BHT/
    """
    _id: Literal["BHT"] = id_element(name="BHT")

    HierarchicalStructureCode: X12ID = element(
        name="BHT01",
        description="Hierarchical Structure Code",
        mandatory=True,
    )

    TransactionSetPurposeCode: X12ID = element(
        name="BHT02",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BHT03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date: Optional[X12DT] = element(
        name="BHT04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BHT05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BHT06",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
