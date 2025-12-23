# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class G54(Segment):
    """
    G54 - Module Description
    
    Description:
        To describe the UPC Case Codes in a module
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G54/
    """
    _id: Literal["G54"] = id_element(name="G54")

    Quantity: X12R = element(
        name="G5401",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="G5402",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    UPCCaseCode: Optional[X12AN] = element(
        name="G5403",
        description="U.P.C. Case Code",
        min_length=12,
        max_length=12,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="G5404",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="G5405",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="G5406",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )
