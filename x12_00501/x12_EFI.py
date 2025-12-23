# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class EFI(Segment):
    """
    EFI - Electronic Format Identification
    
    Description:
        To provide basic information about the electronic format of the interchange data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EFI/
    """
    _id: Literal["EFI"] = id_element(name="EFI")

    SecurityLevelCode: X12ID = element(
        name="EFI01",
        description="Security Level Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="EFI02",
        description="Free-form Message Text",
        min_length=1,
        max_length=264,
    )

    SecurityTechniqueCode: Optional[X12ID] = element(
        name="EFI03",
        description="Security Technique Code",
        min_length=2,
        max_length=2,
    )

    VersionIdentifier: Optional[X12AN] = element(
        name="EFI04",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    ProgramIdentifier: Optional[X12AN] = element(
        name="EFI05",
        description="Program Identifier",
        min_length=1,
        max_length=30,
    )

    VersionIdentifier2: Optional[X12AN] = element(
        name="EFI06",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    InterchangeFormat: Optional[X12AN] = element(
        name="EFI07",
        description="Interchange Format",
        min_length=1,
        max_length=30,
    )

    VersionIdentifier3: Optional[X12AN] = element(
        name="EFI08",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    CompressionTechnique: Optional[X12AN] = element(
        name="EFI09",
        description="Compression Technique",
        min_length=1,
        max_length=30,
    )

    DrawingSheetSizeCode: Optional[X12AN] = element(
        name="EFI10",
        description="Drawing Sheet Size Code",
        min_length=2,
        max_length=2,
    )

    FileName: Optional[X12AN] = element(
        name="EFI11",
        description="File Name",
        min_length=1,
        max_length=64,
    )

    BlockType: Optional[X12AN] = element(
        name="EFI12",
        description="Block Type",
        min_length=1,
        max_length=4,
    )

    RecordLength: Optional[X12Nn] = element(
        name="EFI13",
        description="Record Length",
        min_length=1,
        max_length=15,
    )

    BlockLength: Optional[X12Nn] = element(
        name="EFI14",
        description="Block Length",
        min_length=1,
        max_length=5,
    )

    VersionIdentifier4: Optional[X12AN] = element(
        name="EFI15",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    FilterIDCode: Optional[X12ID] = element(
        name="EFI16",
        description="Filter ID Code",
        min_length=3,
        max_length=3,
    )
