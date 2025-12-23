# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class SPI(Segment):
    """
    SPI - Specification Identifier
    
    Description:
        To provide a description of the included specification or technical data items
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SPI/
    """
    _id: Literal["SPI"] = id_element(name="SPI")

    SecurityLevelCode: X12ID = element(
        name="SPI01",
        description="Security Level Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="SPI02",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="SPI03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    EntityTitle: Optional[X12AN] = element(
        name="SPI04",
        description="Entity Title",
        min_length=1,
        max_length=132,
    )

    EntityPurpose: Optional[X12AN] = element(
        name="SPI05",
        description="Entity Purpose",
        min_length=1,
        max_length=80,
    )

    EntityStatusCode: Optional[X12ID] = element(
        name="SPI06",
        description="Entity Status Code",
        min_length=1,
        max_length=1,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="SPI07",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ReportTypeCode: Optional[X12ID] = element(
        name="SPI08",
        description="Report Type Code",
        min_length=2,
        max_length=2,
    )

    SecurityLevelCode2: Optional[X12ID] = element(
        name="SPI09",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="SPI10",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="SPI11",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="SPI12",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )

    CertificationTypeCode: Optional[X12ID] = element(
        name="SPI13",
        description="Certification Type Code",
        min_length=1,
        max_length=1,
    )

    ProposalDataDetailIdentifierCode: Optional[X12ID] = element(
        name="SPI14",
        description="Proposal Data Detail Identifier Code",
        min_length=2,
        max_length=2,
    )

    HierarchicalStructureCode: Optional[X12ID] = element(
        name="SPI15",
        description="Hierarchical Structure Code",
    )
