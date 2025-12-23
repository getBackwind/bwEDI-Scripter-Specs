# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class B11(Segment):
    """
    B11 - Beginning Segment for Shipment Status Inquiry
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/B11/
    """
    _id: Literal["B11"] = id_element(name="B11")

    IdentificationCodeQualifier: X12ID = element(
        name="B1101",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="B1102",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    Date: Optional[X12DT] = element(
        name="B1103",
        description="Date",
        min_length=8,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="B1104",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="B1105",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="B1106",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="B1107",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ItemDescriptionType: Optional[X12ID] = element(
        name="B1108",
        description="Item Description Type",
    )

    Description: Optional[X12AN] = element(
        name="B1109",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ServiceLevelCode: Optional[X12ID] = element(
        name="B1110",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    ReportTransmissionCode: Optional[X12ID] = element(
        name="B1111",
        description="Report Transmission Code",
        min_length=1,
        max_length=2,
    )
