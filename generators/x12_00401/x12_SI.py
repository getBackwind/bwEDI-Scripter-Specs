# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SI(Segment):
    """
    SI - Service Characteristic Identification
    
    Description:
        To specify service characteristic data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SI/
    """
    _id: Literal["SI"] = id_element(name="SI")

    AgencyQualifierCode: X12ID = element(
        name="SI01",
        description="Agency Qualifier Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ServiceCharacteristicsQualifier: X12AN = element(
        name="SI02",
        description="Service Characteristics Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="SI03",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier2: Optional[X12AN] = element(
        name="SI04",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="SI05",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier3: Optional[X12AN] = element(
        name="SI06",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="SI07",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier4: Optional[X12AN] = element(
        name="SI08",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="SI09",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier5: Optional[X12AN] = element(
        name="SI10",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID5: Optional[X12AN] = element(
        name="SI11",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier6: Optional[X12AN] = element(
        name="SI12",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID6: Optional[X12AN] = element(
        name="SI13",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier7: Optional[X12AN] = element(
        name="SI14",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID7: Optional[X12AN] = element(
        name="SI15",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier8: Optional[X12AN] = element(
        name="SI16",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID8: Optional[X12AN] = element(
        name="SI17",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier9: Optional[X12AN] = element(
        name="SI18",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID9: Optional[X12AN] = element(
        name="SI19",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ServiceCharacteristicsQualifier10: Optional[X12AN] = element(
        name="SI20",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID10: Optional[X12AN] = element(
        name="SI21",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
