# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class MIR(Segment):
    """
    MIR - Mortgage Insurance Response
    
    Description:
        To determine if mortgage insurance has been approved or declined, and if approved, supply details about the coverage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MIR/
    """
    _id: Literal["MIR"] = id_element(name="MIR")

    MortgageInsuranceApplicationType: X12ID = element(
        name="MIR01",
        description="Mortgage Insurance Application Type",
        mandatory=True,
    )

    UnderwritingDecisionCode: X12ID = element(
        name="MIR02",
        description="Underwriting Decision Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    MortgageInsuranceCertificateTypeCode: Optional[X12ID] = element(
        name="MIR03",
        description="Mortgage Insurance Certificate Type Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="MIR04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="MIR05",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    Amount: Optional[X12Nn] = element(
        name="MIR06",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Quantity: Optional[X12R] = element(
        name="MIR08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PercentageAsDecimal2: Optional[X12R] = element(
        name="MIR09",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    PercentageAsDecimal3: Optional[X12R] = element(
        name="MIR10",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    MortgageInsuranceRenewalOptionCode: Optional[X12ID] = element(
        name="MIR11",
        description="Mortgage Insurance Renewal Option Code",
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="MIR12",
        description="Date",
        min_length=8,
        max_length=8,
    )
