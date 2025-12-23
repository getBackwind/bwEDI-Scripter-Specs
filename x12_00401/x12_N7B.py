# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class N7B(Segment):
    """
    N7B - Additional Equipment Details
    
    Description:
        To identify additional equipment details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/N7B/
    """
    _id: Literal["N7B"] = id_element(name="N7B")

    NumberOfTankCompartments: Optional[X12Nn] = element(
        name="N7B01",
        description="Number of Tank Compartments",
        min_length=1,
        max_length=2,
    )

    LoadingOrDischargeLocationCode: Optional[X12ID] = element(
        name="N7B02",
        description="Loading or Discharge Location Code",
        min_length=1,
        max_length=1,
    )

    VesselMaterialCode: Optional[X12ID] = element(
        name="N7B03",
        description="Vessel Material Code",
        min_length=3,
        max_length=3,
    )

    GasketTypeCode: Optional[X12ID] = element(
        name="N7B04",
        description="Gasket Type Code",
        min_length=3,
        max_length=3,
    )

    TrailerLiningTypeCode: Optional[X12ID] = element(
        name="N7B05",
        description="Trailer Lining Type Code",
        min_length=3,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="N7B06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
