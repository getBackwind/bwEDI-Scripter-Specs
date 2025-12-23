# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class PSC(Segment):
    """
    PSC - Product Service Contract
    
    Description:
        To describe the conditions of a product service contract as in a warranty registration
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PSC/
    """
    _id: Literal["PSC"] = id_element(name="PSC")

    ContractStatusCode: X12ID = element(
        name="PSC01",
        description="Contract Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TypeOfProductServiceCode: X12ID = element(
        name="PSC02",
        description="Type of Product Service Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TypeOfProductServiceCode2: Optional[X12ID] = element(
        name="PSC03",
        description="Type of Product Service Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PSC04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="PSC05",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    ContractNumber: Optional[X12AN] = element(
        name="PSC06",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    Count: Optional[X12Nn] = element(
        name="PSC08",
        description="Count",
        min_length=1,
        max_length=9,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="PSC09",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="PSC10",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="PSC11",
        description="Date",
        min_length=8,
        max_length=8,
    )

    RangeMaximum: Optional[X12R] = element(
        name="PSC13",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    RangeMinimum: Optional[X12R] = element(
        name="PSC14",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    MeasurementValue: Optional[X12R] = element(
        name="PSC15",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    ActionCode: Optional[X12ID] = element(
        name="PSC16",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="PSC17",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="PSC18",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="PSC19",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    OperationEnvironmentCode: Optional[X12AN] = element(
        name="PSC20",
        description="Operation Environment Code",
        min_length=2,
        max_length=3,
    )

    SpecialServicesCode: Optional[X12ID] = element(
        name="PSC21",
        description="Special Services Code",
        min_length=2,
        max_length=3,
    )

    Description: Optional[X12AN] = element(
        name="PSC22",
        description="Description",
        min_length=1,
        max_length=80,
    )

    UnitPrice: Optional[X12R] = element(
        name="PSC23",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PSC24",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ContactMethodCode: Optional[X12ID] = element(
        name="PSC25",
        description="Contact Method Code",
        min_length=1,
        max_length=1,
    )
