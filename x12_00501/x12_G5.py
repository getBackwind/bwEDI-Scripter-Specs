# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class G5(Segment):
    """
    G5 - Scale Information
    
    Description:
        To transmit scale information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G5/
    """
    _id: Literal["G5"] = id_element(name="G5")

    EquipmentInitial: X12AN = element(
        name="G501",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="G502",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    WaybillNumber: Optional[X12Nn] = element(
        name="G503",
        description="Waybill Number",
        min_length=1,
        max_length=6,
    )

    Date: Optional[X12DT] = element(
        name="G504",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Weight: X12R = element(
        name="G505",
        description="Weight",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    WeightQualifier: X12ID = element(
        name="G506",
        description="Weight Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    TareWeight: Optional[X12Nn] = element(
        name="G507",
        description="Tare Weight",
        min_length=3,
        max_length=8,
    )

    TareQualifierCode: Optional[X12ID] = element(
        name="G508",
        description="Tare Qualifier Code",
        min_length=1,
        max_length=1,
    )

    WeightAllowance: Optional[X12Nn] = element(
        name="G509",
        description="Weight Allowance",
        min_length=2,
        max_length=6,
    )

    WeightAllowanceTypeCode: Optional[X12ID] = element(
        name="G510",
        description="Weight Allowance Type Code",
        min_length=1,
        max_length=1,
    )

    FreightRate: Optional[X12R] = element(
        name="G511",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="G512",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    InterchangeTrainIdentification: Optional[X12AN] = element(
        name="G513",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )

    CommodityCode: Optional[X12AN] = element(
        name="G514",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="G515",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="G516",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date2: Optional[X12DT] = element(
        name="G517",
        description="Date",
        min_length=8,
        max_length=8,
    )
