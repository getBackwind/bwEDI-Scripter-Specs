# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class IK5(Segment):
    """
    IK5 - Implementation Transaction Set Response Trailer
    
    Description:
        To acknowledge acceptance or rejection and report implementation errors in a transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IK5/
    """
    _id: Literal["IK5"] = id_element(name="IK5")

    TransactionSetAcknowledgmentCode: X12ID = element(
        name="IK501",
        description="Transaction Set Acknowledgment Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ImplementationTransactionSetSyntaxErrorCode: Optional[X12ID] = element(
        name="IK502",
        description="Implementation Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ImplementationTransactionSetSyntaxErrorCode2: Optional[X12ID] = element(
        name="IK503",
        description="Implementation Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ImplementationTransactionSetSyntaxErrorCode3: Optional[X12ID] = element(
        name="IK504",
        description="Implementation Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ImplementationTransactionSetSyntaxErrorCode4: Optional[X12ID] = element(
        name="IK505",
        description="Implementation Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )

    ImplementationTransactionSetSyntaxErrorCode5: Optional[X12ID] = element(
        name="IK506",
        description="Implementation Transaction Set Syntax Error Code",
        min_length=1,
        max_length=2,
    )
