# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class PI(Segment):
    """
    PI - Price Authority Identification
    
    Description:
        To communicate basis of pricing, such as contract number, quote number, or tariff number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PI/
    """
    _id: Literal["PI"] = id_element(name="PI")

    ReferenceIdentificationQualifier: X12ID = element(
        name="PI01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="PI02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    PrimaryPublicationAuthorityCode: Optional[X12ID] = element(
        name="PI03",
        description="Primary Publication Authority Code",
        min_length=2,
        max_length=2,
    )

    RegulatoryAgencyCode: Optional[X12ID] = element(
        name="PI04",
        description="Regulatory Agency Code",
        min_length=3,
        max_length=5,
    )

    TariffAgencyCode: Optional[X12ID] = element(
        name="PI05",
        description="Tariff Agency Code",
        min_length=1,
        max_length=4,
    )

    IssuingCarrierIdentifier: Optional[X12AN] = element(
        name="PI06",
        description="Issuing Carrier Identifier",
        min_length=1,
        max_length=10,
    )

    ContractSuffix: Optional[X12AN] = element(
        name="PI07",
        description="Contract Suffix",
        min_length=1,
        max_length=2,
    )

    TariffItemNumber: Optional[X12AN] = element(
        name="PI08",
        description="Tariff Item Number",
        min_length=1,
        max_length=16,
    )

    TariffSupplementIdentifier: Optional[X12AN] = element(
        name="PI09",
        description="Tariff Supplement Identifier",
        min_length=1,
        max_length=4,
    )

    TariffSection: Optional[X12AN] = element(
        name="PI10",
        description="Tariff Section",
        min_length=1,
        max_length=2,
    )

    ContractSuffix2: Optional[X12AN] = element(
        name="PI11",
        description="Contract Suffix",
        min_length=1,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="PI12",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="PI13",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AlternationPrecedenceCode: Optional[X12ID] = element(
        name="PI14",
        description="Alternation Precedence Code",
        min_length=1,
        max_length=1,
    )

    AlternationPrecedenceCode2: Optional[X12ID] = element(
        name="PI15",
        description="Alternation Precedence Code",
        min_length=1,
        max_length=1,
    )
