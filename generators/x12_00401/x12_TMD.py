# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class TMD(Segment):
    """
    TMD - Test Method
    
    Description:
        To describe the nature of the test performed
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TMD/
    """
    _id: Literal["TMD"] = id_element(name="TMD")

    ProductProcessCharacteristicCode: Optional[X12ID] = element(
        name="TMD01",
        description="Product/Process Characteristic Code",
        min_length=2,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="TMD02",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    ProductDescriptionCode: Optional[X12AN] = element(
        name="TMD03",
        description="Product Description Code",
        min_length=1,
        max_length=12,
    )

    TestAdministrationMethodCode: Optional[X12ID] = element(
        name="TMD04",
        description="Test Administration Method Code",
        min_length=2,
        max_length=2,
    )

    TestMediumCode: Optional[X12ID] = element(
        name="TMD05",
        description="Test Medium Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="TMD06",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Date: Optional[X12DT] = element(
        name="TMD07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="TMD08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="TMD09",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )
