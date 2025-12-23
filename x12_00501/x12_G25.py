# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G25(Segment):
    """
    G25 - F.O.B. Information
    
    Description:
        To transmit information pertaining to method of freight payment and transfer of title
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G25/
    """
    _id: Literal["G25"] = id_element(name="G25")

    ShipmentMethodOfPayment: X12ID = element(
        name="G2501",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    FOBPointCode: X12ID = element(
        name="G2502",
        description="F.O.B. Point Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    FOBPoint: Optional[X12AN] = element(
        name="G2503",
        description="F.O.B. Point",
        min_length=1,
        max_length=30,
    )
