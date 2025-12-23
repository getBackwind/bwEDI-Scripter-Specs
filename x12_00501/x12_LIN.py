# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LIN(Segment):
    """
    LIN - Item Identification
    
    Description:
        To specify basic item identification data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LIN/
    """
    _id: Literal["LIN"] = id_element(name="LIN")

    LineID: Optional[X12AN] = element(
        name="LIN01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    ItemIdQualifier: X12ID = element(
        name="LIN02",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ItemID: X12AN = element(
        name="LIN03",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier2: Optional[X12ID] = element(
        name="LIN04",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID2: Optional[X12AN] = element(
        name="LIN05",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier3: Optional[X12ID] = element(
        name="LIN06",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID3: Optional[X12AN] = element(
        name="LIN07",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier4: Optional[X12ID] = element(
        name="LIN08",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID4: Optional[X12AN] = element(
        name="LIN09",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier5: Optional[X12ID] = element(
        name="LIN10",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID5: Optional[X12AN] = element(
        name="LIN11",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier6: Optional[X12ID] = element(
        name="LIN12",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID6: Optional[X12AN] = element(
        name="LIN13",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier7: Optional[X12ID] = element(
        name="LIN14",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID7: Optional[X12AN] = element(
        name="LIN15",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier8: Optional[X12ID] = element(
        name="LIN16",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID8: Optional[X12AN] = element(
        name="LIN17",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier9: Optional[X12ID] = element(
        name="LIN18",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID9: Optional[X12AN] = element(
        name="LIN19",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier10: Optional[X12ID] = element(
        name="LIN20",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID10: Optional[X12AN] = element(
        name="LIN21",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier11: Optional[X12ID] = element(
        name="LIN22",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID11: Optional[X12AN] = element(
        name="LIN23",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier12: Optional[X12ID] = element(
        name="LIN24",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID12: Optional[X12AN] = element(
        name="LIN25",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier13: Optional[X12ID] = element(
        name="LIN26",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID13: Optional[X12AN] = element(
        name="LIN27",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier14: Optional[X12ID] = element(
        name="LIN28",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID14: Optional[X12AN] = element(
        name="LIN29",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ItemIdQualifier15: Optional[X12ID] = element(
        name="LIN30",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ItemID15: Optional[X12AN] = element(
        name="LIN31",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
