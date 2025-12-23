# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class Y2(Segment):
    """
    Y2 - Container Details
    
    Description:
        To specify container information and transportation service to be used
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/Y2/
    """
    _id: Literal["Y2"] = id_element(name="Y2")

    NumberOfContainers: X12Nn = element(
        name="Y201",
        description="Number of Containers",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    ContainerTypeRequestCode: Optional[X12ID] = element(
        name="Y202",
        description="Container Type Request Code",
        min_length=1,
        max_length=1,
    )

    TypeOfServiceCode: Optional[X12ID] = element(
        name="Y203",
        description="Type of Service Code",
        min_length=2,
        max_length=2,
    )

    EquipmentType: X12ID = element(
        name="Y204",
        description="Equipment Type",
        mandatory=True,
        min_length=4,
        max_length=4,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="Y205",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    IntermodalServiceCode: Optional[X12ID] = element(
        name="Y206",
        description="Intermodal Service Code",
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="Y207",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ContainerTermsCode: Optional[X12ID] = element(
        name="Y208",
        description="Container Terms Code",
        min_length=3,
        max_length=3,
    )

    ContainerTermsCodeQualifier: Optional[X12ID] = element(
        name="Y209",
        description="Container Terms Code Qualifier",
        min_length=1,
        max_length=1,
    )

    TotalStopOffs: Optional[X12Nn] = element(
        name="Y210",
        description="Total Stop-offs",
        min_length=1,
        max_length=2,
    )
