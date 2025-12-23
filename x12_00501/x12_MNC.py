# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class MNC(Segment):
    """
    MNC - Mortgage Note Characteristics
    
    Description:
        To provide detailed characteristics information of a mortgage note
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MNC/
    """
    _id: Literal["MNC"] = id_element(name="MNC")

    CodeCategory: Optional[X12ID] = element(
        name="MNC01",
        description="Code Category",
        min_length=2,
        max_length=2,
    )

    RealEstateLoanTypeCode: Optional[X12ID] = element(
        name="MNC02",
        description="Real Estate Loan Type Code",
        min_length=1,
        max_length=1,
    )

    LienPriorityCode: Optional[X12ID] = element(
        name="MNC03",
        description="Lien Priority Code",
        min_length=1,
        max_length=1,
    )

    LoanPaymentTypeCode: Optional[X12ID] = element(
        name="MNC04",
        description="Loan Payment Type Code",
        min_length=2,
        max_length=2,
    )

    LoanRateTypeCode: Optional[X12ID] = element(
        name="MNC05",
        description="Loan Rate Type Code",
        min_length=1,
        max_length=1,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="MNC06",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    InterestRateCalculationMethodCode: Optional[X12ID] = element(
        name="MNC07",
        description="Interest Rate Calculation Method Code",
        min_length=1,
        max_length=1,
    )

    Number: Optional[X12Nn] = element(
        name="MNC08",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number2: Optional[X12Nn] = element(
        name="MNC09",
        description="Number",
        min_length=1,
        max_length=9,
    )

    PaymentMethodTypeCode: Optional[X12ID] = element(
        name="MNC10",
        description="Payment Method Type Code",
        min_length=1,
        max_length=2,
    )

    InterestPaymentCode: Optional[X12ID] = element(
        name="MNC11",
        description="Interest Payment Code",
        min_length=1,
        max_length=1,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="MNC12",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="MNC13",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductProcessCharacteristicCode: Optional[X12ID] = element(
        name="MNC14",
        description="Product/Process Characteristic Code",
        min_length=2,
        max_length=3,
    )

    ProductDescriptionCode: Optional[X12AN] = element(
        name="MNC15",
        description="Product Description Code",
        min_length=1,
        max_length=12,
    )

    TypeOfRealEstateAssetCode: Optional[X12ID] = element(
        name="MNC16",
        description="Type of Real Estate Asset Code",
        min_length=2,
        max_length=2,
    )

    RealEstateLoanSecurityInstrumentCode: Optional[X12ID] = element(
        name="MNC17",
        description="Real Estate Loan Security Instrument Code",
        min_length=1,
        max_length=1,
    )
