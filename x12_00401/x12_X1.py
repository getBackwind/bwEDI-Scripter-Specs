# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class X1(Segment):
    """
    X1 - Export License
    
    Description:
        To transmit information contained on an export license
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/X1/
    """
    _id: Literal["X1"] = id_element(name="X1")

    LicensingAgencyCode: Optional[X12ID] = element(
        name="X101",
        description="Licensing Agency Code",
    )

    ExportLicenseNumber: Optional[X12AN] = element(
        name="X102",
        description="Export License Number",
        min_length=6,
        max_length=12,
    )

    ExportLicenseStatusCode: Optional[X12ID] = element(
        name="X103",
        description="Export License Status Code",
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="X104",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ExportLicenseSymbolCode: Optional[X12ID] = element(
        name="X105",
        description="Export License Symbol Code",
        min_length=1,
        max_length=2,
    )

    ExportLicenseControlCode: Optional[X12ID] = element(
        name="X106",
        description="Export License Control Code",
        min_length=1,
        max_length=1,
    )

    CountryCode: Optional[X12ID] = element(
        name="X107",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    ScheduleBCode: Optional[X12ID] = element(
        name="X108",
        description="Schedule B Code",
        min_length=7,
        max_length=10,
    )

    InternationalDomesticCode: Optional[X12ID] = element(
        name="X109",
        description="International/Domestic Code",
        min_length=1,
        max_length=1,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="X110",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    LadingValue: Optional[X12R] = element(
        name="X111",
        description="Lading Value",
        min_length=2,
        max_length=9,
    )

    ExportFilingKeyCode: Optional[X12ID] = element(
        name="X112",
        description="Export Filing Key Code",
        min_length=1,
        max_length=1,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="X113",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UnitPrice: Optional[X12R] = element(
        name="X114",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    USGovernmentLicenseType: Optional[X12AN] = element(
        name="X115",
        description="U.S. Government License Type",
        min_length=1,
        max_length=1,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="X116",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
