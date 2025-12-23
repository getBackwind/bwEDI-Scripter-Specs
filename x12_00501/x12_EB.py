# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class EB(Segment):
    """
    EB - Eligibility or Benefit Information
    
    Description:
        To supply eligibility or benefit information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EB/
    """
    _id: Literal["EB"] = id_element(name="EB")

    EligibilityOrBenefitInformationCode: X12ID = element(
        name="EB01",
        description="Eligibility or Benefit Information Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CoverageLevelCode: Optional[X12ID] = element(
        name="EB02",
        description="Coverage Level Code",
        min_length=3,
        max_length=3,
    )

    ServiceTypeCode: Optional[X12ID] = element(
        name="EB03",
        description="Service Type Code",
        min_length=1,
        max_length=2,
    )

    InsuranceTypeCode: Optional[X12ID] = element(
        name="EB04",
        description="Insurance Type Code",
        min_length=1,
        max_length=2,
    )

    PlanCoverageDescription: Optional[X12AN] = element(
        name="EB05",
        description="Plan Coverage Description",
        min_length=1,
        max_length=50,
    )

    TimePeriodQualifier: Optional[X12ID] = element(
        name="EB06",
        description="Time Period Qualifier",
        min_length=1,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="EB07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="EB08",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="EB09",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="EB10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="EB11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="EB12",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ProductServiceIDQualifier: X12ID = element(
        name="EB1301",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="EB1302",
        description="Product/Service ID",
        mandatory=True,
        min_length=0,
        max_length=48,
    )

    ProcedureModifier: Optional[X12AN] = element(
        name="EB1303",
        description="Procedure Modifier",
        min_length=2,
        max_length=2,
    )

    ProcedureModifier2: Optional[X12AN] = element(
        name="EB1304",
        description="Procedure Modifier",
        min_length=2,
        max_length=2,
    )

    ProcedureModifier3: Optional[X12AN] = element(
        name="EB1305",
        description="Procedure Modifier",
        min_length=2,
        max_length=2,
    )

    ProcedureModifier4: Optional[X12AN] = element(
        name="EB1306",
        description="Procedure Modifier",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="EB1307",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="EB1308",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    DiagnosisCodePointer: X12Nn = element(
        name="EB1401",
        description="Diagnosis Code Pointer",
        mandatory=True,
        min_length=0,
        max_length=2,
    )

    DiagnosisCodePointer2: Optional[X12Nn] = element(
        name="EB1402",
        description="Diagnosis Code Pointer",
        min_length=1,
        max_length=2,
    )

    DiagnosisCodePointer3: Optional[X12Nn] = element(
        name="EB1403",
        description="Diagnosis Code Pointer",
        min_length=1,
        max_length=2,
    )

    DiagnosisCodePointer4: Optional[X12Nn] = element(
        name="EB1404",
        description="Diagnosis Code Pointer",
        min_length=1,
        max_length=2,
    )
