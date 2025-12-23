# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class PRI(Segment):
    """
    PRI - External Reference Identifier
    
    Description:
        To identify an external reference
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PRI/
    """
    _id: Literal["PRI"] = id_element(name="PRI")

    PrimaryPublicationAuthorityCode: X12ID = element(
        name="PRI01",
        description="Primary Publication Authority Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TariffAgencyCode: X12ID = element(
        name="PRI02",
        description="Tariff Agency Code",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    TariffNumber: X12AN = element(
        name="PRI03",
        description="Tariff Number",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    TariffNumberSuffix: Optional[X12AN] = element(
        name="PRI04",
        description="Tariff Number Suffix",
        min_length=1,
        max_length=2,
    )

    TariffSupplementIdentifier: Optional[X12AN] = element(
        name="PRI05",
        description="Tariff Supplement Identifier",
        min_length=1,
        max_length=4,
    )

    TariffSectionNumber: Optional[X12AN] = element(
        name="PRI06",
        description="Tariff Section Number",
        min_length=1,
        max_length=2,
    )

    TariffItemNumber: Optional[X12AN] = element(
        name="PRI07",
        description="Tariff Item Number",
        min_length=1,
        max_length=16,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="PRI08",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PRI09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="PRI10",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    DocketControlNumber: Optional[X12AN] = element(
        name="PRI11",
        description="Docket Control Number",
        min_length=1,
        max_length=7,
    )

    DocketIdentification: Optional[X12AN] = element(
        name="PRI12",
        description="Docket Identification",
        min_length=1,
        max_length=11,
    )

    RevisionNumber: Optional[X12Nn] = element(
        name="PRI13",
        description="Revision Number",
        min_length=1,
        max_length=4,
    )

    GroupTitle: Optional[X12AN] = element(
        name="PRI14",
        description="Group Title",
        min_length=2,
        max_length=30,
    )
