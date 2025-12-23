# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class F09(Segment):
    """
    F09 - Detail - Supporting Evidence for Claim
    
    Description:
        To specify the extent of damage and the amount claimed for damaged goods
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/F09/
    """
    _id: Literal["F09"] = id_element(name="F09")

    Quantity: X12R = element(
        name="F0901",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="F0902",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    NatureOfClaimCode: X12ID = element(
        name="F0903",
        description="Nature of Claim Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Amount: X12Nn = element(
        name="F0904",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Amount2: X12Nn = element(
        name="F0905",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="F0906",
        description="Description",
        min_length=1,
        max_length=80,
    )

    LadingDescription: Optional[X12AN] = element(
        name="F0907",
        description="Lading Description",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="F0908",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="F0909",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="F0910",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="F0911",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    LadingLineItemNumber: Optional[X12Nn] = element(
        name="F0912",
        description="Lading Line Item Number",
        min_length=1,
        max_length=3,
    )
