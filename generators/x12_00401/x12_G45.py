# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class G45(Segment):
    """
    G45 - Line Item Detail - Promotion
    
    Description:
        To provide information for a line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G45/
    """
    _id: Literal["G45"] = id_element(name="G45")

    UPCCaseCode: Optional[X12AN] = element(
        name="G4501",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    UPCEANConsumerPackageCode: Optional[X12AN] = element(
        name="G4502",
        description="U.P.C./EAN Consumer Package Code",
        min_length=12,
        max_length=12,
    )

    AllowanceOrChargeNumber: Optional[X12AN] = element(
        name="G4503",
        description="Allowance or Charge Number",
        min_length=1,
        max_length=16,
    )

    ExceptionNumber: Optional[X12AN] = element(
        name="G4504",
        description="Exception Number",
        min_length=1,
        max_length=16,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G4505",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G4506",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Pack: Optional[X12Nn] = element(
        name="G4507",
        description="Pack",
        min_length=1,
        max_length=6,
    )

    Size: Optional[X12R] = element(
        name="G4508",
        description="Size",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G4509",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    DateQualifier: Optional[X12ID] = element(
        name="G4510",
        description="Date Qualifier",
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="G4511",
        description="Date",
        min_length=8,
        max_length=8,
    )

    InnerPack: Optional[X12Nn] = element(
        name="G4512",
        description="Inner Pack",
        min_length=1,
        max_length=6,
    )

    AllowanceOrChargeRate: Optional[X12R] = element(
        name="G4513",
        description="Allowance or Charge Rate",
        min_length=1,
        max_length=15,
    )
