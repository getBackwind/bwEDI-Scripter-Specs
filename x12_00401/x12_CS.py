# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CS(Segment):
    """
    CS - Contract Summary
    
    Description:
        To provide information about a contract
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CS/
    """
    _id: Literal["CS"] = id_element(name="CS")

    ContractNumber: Optional[X12AN] = element(
        name="CS01",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    ChangeOrderSequenceNumber: Optional[X12AN] = element(
        name="CS02",
        description="Change Order Sequence Number",
        min_length=1,
        max_length=8,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="CS03",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="CS04",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CS05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="CS06",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    SpecialServicesCode: Optional[X12ID] = element(
        name="CS07",
        description="Special Services Code",
        min_length=2,
        max_length=3,
    )

    FOBPointCode: Optional[X12ID] = element(
        name="CS08",
        description="F.O.B. Point Code",
        min_length=2,
        max_length=2,
    )

    Percent: Optional[X12R] = element(
        name="CS09",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    Percent2: Optional[X12R] = element(
        name="CS10",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="CS11",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    TermsTypeCode: Optional[X12ID] = element(
        name="CS12",
        description="Terms Type Code",
        min_length=2,
        max_length=2,
    )

    SpecialServicesCode2: Optional[X12ID] = element(
        name="CS13",
        description="Special Services Code",
        min_length=2,
        max_length=3,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="CS14",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UnitPrice: Optional[X12R] = element(
        name="CS15",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    TermsTypeCode2: Optional[X12ID] = element(
        name="CS16",
        description="Terms Type Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CS17",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="CS18",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
