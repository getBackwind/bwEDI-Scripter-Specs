# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class E10(Segment):
    """
    E10 - Transaction Set Grouping
    
    Description:
        To provide information grouping of transaction sets by transaction ID and functional ID for the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E10/
    """
    _id: Literal["E10"] = id_element(name="E10")

    MaintenanceOperationCode: X12ID = element(
        name="E1001",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    TransactionSetIdentifierCode: X12ID = element(
        name="E1002",
        description="Transaction Set Identifier Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    FunctionalIdentifierCode: X12ID = element(
        name="E1003",
        description="Functional Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Description: X12AN = element(
        name="E1004",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="E1005",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )
