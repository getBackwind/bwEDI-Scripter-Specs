# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class F07(Segment):
    """
    F07 - Auto Claim Detail
    
    Description:
        To itemize extent of automotive loss or damage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/F07/
    """
    _id: Literal["F07"] = id_element(name="F07")

    AssignedNumber: X12Nn = element(
        name="F0701",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    Quantity: Optional[X12R] = element(
        name="F0702",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="F0703",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    PartName: Optional[X12AN] = element(
        name="F0704",
        description="Part Name",
        min_length=3,
        max_length=16,
    )

    Amount: Optional[X12Nn] = element(
        name="F0705",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    DamageAreaCode: X12ID = element(
        name="F0706",
        description="Damage Area Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DamageTypeCode: X12ID = element(
        name="F0707",
        description="Damage Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DamageSeverityCode: X12ID = element(
        name="F0708",
        description="Damage Severity Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    LaborOperationIdentifier: Optional[X12AN] = element(
        name="F0709",
        description="Labor Operation Identifier",
        min_length=5,
        max_length=6,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="F0710",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    LaborHours: Optional[X12Nn] = element(
        name="F0711",
        description="Labor Hours",
        min_length=1,
        max_length=3,
    )

    LaborHours2: Optional[X12Nn] = element(
        name="F0712",
        description="Labor Hours",
        min_length=1,
        max_length=3,
    )

    TotalLaborCost: Optional[X12Nn] = element(
        name="F0713",
        description="Total Labor Cost",
        min_length=3,
        max_length=6,
    )

    TotalMiscellaneousCosts: Optional[X12Nn] = element(
        name="F0714",
        description="Total Miscellaneous Costs",
        min_length=2,
        max_length=15,
    )

    TotalRepairCost: X12Nn = element(
        name="F0715",
        description="Total Repair Cost",
        mandatory=True,
        min_length=3,
        max_length=15,
    )

    AuthorizationIdentification: Optional[X12AN] = element(
        name="F0716",
        description="Authorization Identification",
        min_length=1,
        max_length=4,
    )

    InspectionLocationTypeCode: Optional[X12ID] = element(
        name="F0717",
        description="Inspection Location Type Code",
        min_length=1,
        max_length=2,
    )

    DamageAreaCode2: Optional[X12ID] = element(
        name="F0718",
        description="Damage Area Code",
        min_length=2,
        max_length=2,
    )

    DamageTypeCode2: Optional[X12ID] = element(
        name="F0719",
        description="Damage Type Code",
        min_length=2,
        max_length=2,
    )

    DamageSeverityCode2: Optional[X12ID] = element(
        name="F0720",
        description="Damage Severity Code",
        min_length=1,
        max_length=1,
    )

    DeclineAmendReasonCode: Optional[X12ID] = element(
        name="F0721",
        description="Decline/Amend Reason Code",
        min_length=3,
        max_length=3,
    )

    ChargeAllowanceQualifier: Optional[X12ID] = element(
        name="F0722",
        description="Charge/Allowance Qualifier",
        min_length=2,
        max_length=2,
    )
