# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class FK(Segment):
    """
    FK - Factor
    
    Description:
        To explain the route and indicate individual carrier divisions or factors
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FK/
    """
    _id: Literal["FK"] = id_element(name="FK")

    StandardCarrierAlphaCode: X12ID = element(
        name="FK01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    TransportationMethodTypeCode: X12ID = element(
        name="FK02",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="FK03",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="FK04",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    Rule260JunctionCode: Optional[X12ID] = element(
        name="FK05",
        description="Rule 260 Junction Code",
        min_length=1,
        max_length=5,
    )

    PercentageDivision: Optional[X12Nn] = element(
        name="FK06",
        description="Percentage Division",
        min_length=1,
        max_length=5,
    )

    FactorAmount: Optional[X12R] = element(
        name="FK07",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )

    FactorAmount2: Optional[X12R] = element(
        name="FK08",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )

    FactorAmount3: Optional[X12R] = element(
        name="FK09",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )

    FactorAmount4: Optional[X12R] = element(
        name="FK10",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )

    FactorAmount5: Optional[X12R] = element(
        name="FK11",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )

    FactorAmount6: Optional[X12R] = element(
        name="FK12",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )

    FactorAmount7: Optional[X12R] = element(
        name="FK13",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )

    FactorAmount8: Optional[X12R] = element(
        name="FK14",
        description="Factor Amount",
        min_length=1,
        max_length=9,
    )
