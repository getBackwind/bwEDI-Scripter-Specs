# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class ACK(Segment):
    """
    ACK - Line Item Acknowledgment
    
    Description:
        To acknowledge the ordered quantities and specify the ready date for a specific line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ACK/
    """
    _id: Literal["ACK"] = id_element(name="ACK")

    ItemStatus: X12ID = element(
        name="ACK01",
        description="Line Item Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="ACK02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UOM: Optional[X12ID] = element(
        name="ACK03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="ACK04",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="ACK05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    RequestReferenceNumber: Optional[X12AN] = element(
        name="ACK06",
        description="Request Reference Number",
        min_length=1,
        max_length=45,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="ACK07",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="ACK08",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier2: Optional[X12ID] = element(
        name="ACK09",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="ACK10",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier3: Optional[X12ID] = element(
        name="ACK11",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID3: Optional[X12AN] = element(
        name="ACK12",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier4: Optional[X12ID] = element(
        name="ACK13",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID4: Optional[X12AN] = element(
        name="ACK14",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier5: Optional[X12ID] = element(
        name="ACK15",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID5: Optional[X12AN] = element(
        name="ACK16",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier6: Optional[X12ID] = element(
        name="ACK17",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID6: Optional[X12AN] = element(
        name="ACK18",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier7: Optional[X12ID] = element(
        name="ACK19",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID7: Optional[X12AN] = element(
        name="ACK20",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier8: Optional[X12ID] = element(
        name="ACK21",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID8: Optional[X12AN] = element(
        name="ACK22",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier9: Optional[X12ID] = element(
        name="ACK23",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID9: Optional[X12AN] = element(
        name="ACK24",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceIDQualifier10: Optional[X12ID] = element(
        name="ACK25",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID10: Optional[X12AN] = element(
        name="ACK26",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="ACK27",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="ACK28",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    IndustryCode: Optional[X12AN] = element(
        name="ACK29",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
