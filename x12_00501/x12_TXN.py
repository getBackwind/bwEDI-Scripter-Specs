# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class TXN(Segment):
    """
    TXN - Transaction Capabilities
    
    Description:
        To indicate EDI transaction capabilities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TXN/
    """
    _id: Literal["TXN"] = id_element(name="TXN")

    ActionCode: X12ID = element(
        name="TXN01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ResponsibleAgencyCode: Optional[X12ID] = element(
        name="TXN02",
        description="Responsible Agency Code",
        min_length=1,
        max_length=1,
    )

    TransactionSetIdentifierCode: Optional[X12ID] = element(
        name="TXN03",
        description="Transaction Set Identifier Code",
        min_length=3,
        max_length=3,
    )

    VersionReleaseIndustryIdentifierCode: Optional[X12AN] = element(
        name="TXN04",
        description="Version / Release / Industry Identifier Code",
        min_length=1,
        max_length=12,
    )

    ActionCode2: X12ID = element(
        name="TXN05",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ApplicationReceiverSCode: Optional[X12AN] = element(
        name="TXN06",
        description="Application Receiver's Code",
        min_length=2,
        max_length=15,
    )

    ApplicationSenderSCode: Optional[X12AN] = element(
        name="TXN07",
        description="Application Sender's Code",
        min_length=2,
        max_length=15,
    )

    Date: Optional[X12DT] = element(
        name="TXN08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="TXN09",
        description="Time",
        min_length=4,
        max_length=8,
    )
