# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BCT(Segment):
    """
    BCT - Beginning Segment for Price/Sales Catalog
    
    Description:
        To indicate the beginning of the Price/Sales Catalog Transaction Set and specify catalog purpose and number information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BCT/
    """
    _id: Literal["BCT"] = id_element(name="BCT")

    CatalogPurposeCode: X12ID = element(
        name="BCT01",
        description="Catalog Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CatalogNumber: Optional[X12AN] = element(
        name="BCT02",
        description="Catalog Number",
        min_length=1,
        max_length=15,
    )

    CatalogVersionNumber: Optional[X12AN] = element(
        name="BCT03",
        description="Catalog Version Number",
        min_length=1,
        max_length=15,
    )

    CatalogRevisionNumber: Optional[X12AN] = element(
        name="BCT04",
        description="Catalog Revision Number",
        min_length=1,
        max_length=6,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="BCT05",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    CatalogNumber2: Optional[X12AN] = element(
        name="BCT06",
        description="Catalog Number",
        min_length=1,
        max_length=15,
    )

    CatalogVersionNumber2: Optional[X12AN] = element(
        name="BCT07",
        description="Catalog Version Number",
        min_length=1,
        max_length=15,
    )

    CatalogRevisionNumber2: Optional[X12AN] = element(
        name="BCT08",
        description="Catalog Revision Number",
        min_length=1,
        max_length=6,
    )

    Description: Optional[X12AN] = element(
        name="BCT09",
        description="Description",
        min_length=1,
        max_length=80,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BCT10",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )
